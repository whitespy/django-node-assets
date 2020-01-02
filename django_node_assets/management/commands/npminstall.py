import os
import os.path
import shutil
from subprocess import Popen, PIPE, STDOUT

from django.conf import settings
from django.core.management.base import BaseCommand


class NodePackageContext:

    def __init__(self):
        self.package_dir = os.path.dirname(settings.NODE_MODULES_ROOT)
        self.package_json = os.path.join(self.package_dir, 'package.json')

    def __enter__(self):
        if self.package_json != str(settings.NODE_PACKAGE_JSON):
            shutil.copy(settings.NODE_PACKAGE_JSON, self.package_json)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.package_json != str(settings.NODE_PACKAGE_JSON) and os.path.exists(self.package_json):
            os.remove(self.package_json)
        return False


class Command(BaseCommand):
    help = 'Installs all dependencies listed in the package.json'

    def handle(self, **options):
        if not hasattr(settings, 'NODE_PACKAGE_JSON'):
            self.stderr.write('The NODE_PACKAGE_JSON option is not specified.')
            return
        if not os.path.isfile(settings.NODE_PACKAGE_JSON):
            self.stderr.write('The {} file not found.'.format(settings.NODE_PACKAGE_JSON))
            return
        if not os.path.isdir(settings.NODE_MODULES_ROOT):
            self.stderr.write('The {} directory does not exist.'.format(settings.NODE_MODULES_ROOT))
            return
        with NodePackageContext() as node_package_context:
            with Popen(
                    args=['install', '--no-package-lock', '--prefix={}'.format(node_package_context.package_dir)],
                    executable=getattr(settings, 'NODE_PACKAGE_MANAGER_EXECUTABLE', '/usr/bin/npm'),
                    shell=True,
                    stdout=PIPE,
                    stderr=STDOUT,
            ) as p:
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
