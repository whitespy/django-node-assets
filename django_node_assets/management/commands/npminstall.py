import os
import os.path
from contextlib import contextmanager
from subprocess import Popen, PIPE, STDOUT

from django.conf import settings
from django.core.management.base import BaseCommand

NODE_PACKAGE_DIR = os.path.dirname(settings.NODE_MODULES_ROOT)


@contextmanager
def node_package_context():
    package_json_symlink = os.path.join(NODE_PACKAGE_DIR, 'package.json')
    if package_json_symlink != settings.NODE_PACKAGE_JSON:
        os.symlink(settings.NODE_PACKAGE_JSON, package_json_symlink)
    yield
    if os.path.exists(package_json_symlink) and os.path.islink(package_json_symlink):
        os.unlink(package_json_symlink)


class Command(BaseCommand):
    help = 'Installs all dependencies specified in the package.json'

    def handle(self, **options):
        if not hasattr(settings, 'NODE_PACKAGE_JSON'):
            self.stderr.write('The NODE_PACKAGE_JSON option does not specified.')
            return
        if not os.path.exists(settings.NODE_PACKAGE_JSON):
            self.stderr.write('The package.json not found.')
        with node_package_context():
            with Popen(args=['install', '--no-package-lock', '--prefix={}'.format(NODE_PACKAGE_DIR)],
                       executable=getattr(settings, 'NODE_PACKAGE_MANAGER_EXECUTABLE', '/usr/bin/npm'),
                       shell=True, stdout=PIPE, stderr=STDOUT) as p:
                for line in p.stdout:
                    decoded_line = line.decode()
                    if decoded_line.startswith('npm WARN'):
                        self.stdout.write(self.style.WARNING(decoded_line), ending='')
                    else:
                        self.stdout.write(decoded_line)
        if p.poll() == 0:
            self.stdout.write(self.style.SUCCESS('All dependencies has been successfully installed.'))
        else:
            self.stderr.write('An error occurred.')
