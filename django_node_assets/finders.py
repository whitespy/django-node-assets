import json

from django.conf import settings
from django.contrib.staticfiles.finders import BaseFinder
from django.contrib.staticfiles.utils import get_files
from django.core.files.storage import FileSystemStorage


class NodeModulesFinder(BaseFinder):
    """
    The static files finder that find static files stored
    in the NODE_MODULES_ROOT, and excludes metadata and unwanted files when
    static files will be collected.
    """

    storage = FileSystemStorage(location=settings.NODE_MODULES_ROOT)
    ignore_patterns = [
        "*.less",
        "*.scss",
        "*.styl",
        "*.sh",
        "*.htm",
        "*.html",
        "*.md",
        "*.markdown",
        "*.rst",
        "*.php",
        "*.rb",
        "*.txt",
        "*.map",
        "*.yml",
        "*.yaml",
        "*.json",
        "*.xml",
        "*.ts",
        "*.es6",
        "*.coffee",
        "*.litcoffee",
        "*.lock",
        "*.patch",
        "README*",
        "LICENSE*",
        "LICENCE*",
        "CHANGES",
        "CHANGELOG",
        "HISTORY",
        "NOTICE",
        "COPYING",
        "license",
        "*test*",
        "*bin*",
        "*samples*",
        "*example*",
        "*docs*",
        "*tests*",
        "*demo*",
        "Makefile*",
        "Gemfile*",
        "Gruntfile*",
        "gulpfile.js",
        ".tagconfig",
        ".npmignore",
        ".gitignore",
        ".gitattributes",
        ".gitmodules",
        ".editorconfig",
        ".sqlite",
        "grunt",
        "gulp",
        "less",
        "sass",
        "scss",
        "coffee",
        "tasks",
        "node_modules",
    ]

    def find(self, path, all=False):
        matches = []
        if self.storage.exists(path):
            matched_path = self.storage.path(path)
            if not all:
                return matched_path
            matches.append(matched_path)
        return matches

    def list(self, *args, **kwargs):
        for path in get_files(self.storage, self.ignore_patterns):
            yield path, self.storage


class ManifestNodeModulesFinder(NodeModulesFinder):
    """
    The static files finder that looks in the directory of each dependency
    specified in the package.json and excludes metadata and unwanted files when
    static files will be collected.
    """

    def list(self, *args, **kwargs):
        try:
            with open(settings.NODE_PACKAGE_JSON) as f:
                package_json = json.load(f)
        except IOError:
            for path in get_files(self.storage, self.ignore_patterns):
                yield path, self.storage
        else:
            if "dependencies" in package_json and isinstance(
                package_json["dependencies"], dict
            ):
                node_modules = {
                    node_module for node_module in package_json["dependencies"].keys()
                }
                for module in node_modules:
                    if self.storage.exists(module):
                        for path in get_files(
                            self.storage, self.ignore_patterns, module
                        ):
                            yield path, self.storage
