import json

import django
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

    default_ignore_patterns = [
        "*.coffee",
        "*.es6",
        "*.htm",
        "*.html",
        "*.json",
        "*.less",
        "*.litcoffee",
        "*.lock",
        "*.map",
        "*.markdown",
        "*.md",
        "*.patch",
        "*.php",
        "*.rb",
        "*.rst",
        "*.scss",
        "*.sh",
        "*.styl",
        "*.ts",
        "*.txt",
        "*.xml",
        "*.yaml",
        "*.yml",
        "*bin*",
        "*demo*",
        "*docs*",
        "*example*",
        "*samples*",
        "*test*",
        "*tests*",
        ".editorconfig",
        ".gitattributes",
        ".gitignore",
        ".gitmodules",
        ".npmignore",
        ".sqlite",
        ".tagconfig",
        "CHANGELOG",
        "CHANGES",
        "COPYING",
        "Gemfile*",
        "Gruntfile*",
        "HISTORY",
        "LICENCE*",
        "LICENSE*",
        "Makefile*",
        "NOTICE",
        "README*",
        "coffee",
        "grunt",
        "gulp",
        "gulpfile.js",
        "less",
        "license",
        "node_modules",
        "sass",
        "scss",
        "tasks",
    ]

    def __init__(self, *args, **kwargs):
        self.storage = FileSystemStorage(location=settings.NODE_MODULES_ROOT)

    def find(self, path, **kwargs):
        if django.VERSION >= (5, 2):
            find_all = kwargs.get("find_all", False)
        else:
            find_all = kwargs.get("all", False)

        matches = []

        if self.storage.exists(path):
            matched_path = self.storage.path(path)

            if not find_all:
                return matched_path

            matches.append(matched_path)

        return matches

    def list(self, ignore_patterns):
        ignore_patterns = {*self.default_ignore_patterns, *ignore_patterns}

        for path in get_files(storage=self.storage, ignore_patterns=ignore_patterns):
            yield path, self.storage


class ManifestNodeModulesFinder(NodeModulesFinder):
    """
    The static files finder that looks in the directory of each dependency
    specified in the package.json and excludes metadata and unwanted files when
    static files will be collected.
    """

    def list(self, ignore_patterns):
        try:
            with open(settings.NODE_PACKAGE_JSON, encoding="utf-8") as f:
                package_json = json.load(f)
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            return None

        package_json_dependencies = package_json.get("dependencies", {})

        ignore_patterns = {*self.default_ignore_patterns, *ignore_patterns}

        for dependency in package_json_dependencies:
            if self.storage.exists(dependency):
                for path in get_files(
                    storage=self.storage,
                    ignore_patterns=ignore_patterns,
                    location=dependency,
                ):
                    yield path, self.storage
