#!/usr/bin/env python
# setup
# Installs and maintains the Python package
#
# Author:   PingThings
# Created:  Tue Nov 26 11:52:24 2019 -0500
#
# For license information, see LICENSE.txt
# ID: setup.py [] benjamin@pingthings.io $

"""
Installs and maintains the Python package
"""

##########################################################################
## Imports
##########################################################################

import os
import codecs

from setuptools import setup
from setuptools import find_packages


##########################################################################
## Configuration
##########################################################################

NAME         = "jupyteranalytics"
DESCRIPTION  = "Adds Google Analytics to Jupyter notebooks"
AUTHOR       = "PingThings, Inc."
EMAIL        = "support@pingthings.io"
LICENSE      = "BSD-3-Clause"
REPOSITORY   = "https://github.com/PingThingsIO/jupyter-analytics"
PACKAGE      = "jupyteranalytics"
KEYWORDS     = ("Google Analytics", "notebooks", "Jupyter", "JupyterHub")

## Define the classifiers
## See https://pypi.python.org/pypi?%3Aaction=list_classifiers
CLASSIFIERS  = (
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Framework :: Jupyter',
    'Intended Audience :: Developers',
    'Intended Audience :: Science/Research',
    'Intended Audience :: System Administrators',
    'License :: OSI Approved :: BSD License',
    'Natural Language :: English',
    'Operating System :: OS Independent',
    'Programming Language :: Python'
)

PROJECT      = os.path.abspath(os.path.dirname(__file__))
REQUIRE_PATH = "requirements.txt"
VERSION_PATH = os.path.join(PACKAGE, "version.py")
PKG_DESCRIBE = "README.md"
EXCLUDES     = ("tests", "docs", "fixtures")

##########################################################################
## Helper Functions
##########################################################################

def read(*parts):
    """
    Assume UTF-8 encoding and return the contents of the file located at the
    absolute path from the REPOSITORY joined with *parts.
    """
    with codecs.open(os.path.join(PROJECT, *parts), 'rb', 'utf-8') as f:
        return f.read()


def get_version(path=VERSION_PATH):
    """
    Reads the python file defined in the VERSION_PATH to find the get_version
    function, and executes it to ensure that it is loaded correctly. Separating
    the version in this way ensures no additional code is executed.
    """
    namespace = {}
    exec(read(path), namespace)
    return namespace['get_version'](short=True)


def get_requires(path=REQUIRE_PATH):
    """
    Yields a generator of requirements as defined by the REQUIRE_PATH which
    should point to a requirements.txt output by `pip freeze`.
    """
    for line in read(path).splitlines():
        line = line.strip()
        if line and not line.startswith('#'):
            yield line


def get_description_type(path=PKG_DESCRIBE):
    """
    Returns the long_description_content_type based on the extension of the
    package describe path (e.g. .txt, .rst, or .md).
    """
    _, ext = os.path.splitext(path)
    return {
        ".rst": "text/x-rst",
        ".txt": "text/plain",
        ".md": "text/markdown",
    }[ext]


##########################################################################
## Define the configuration
##########################################################################

config = {
    "name": NAME,
    "version": get_version(),
    "description": DESCRIPTION,
    "long_description": read(PKG_DESCRIBE),
    "long_description_content_type": get_description_type(PKG_DESCRIBE),
    "classifiers": list(CLASSIFIERS),
    "keywords": list(KEYWORDS),
    "license": LICENSE,
    "author": AUTHOR,
    "author_email": EMAIL,
    "maintainer": AUTHOR,
    "maintainer_email": EMAIL,
    "project_urls": {
        "Download": "{}/tarball/v{}".format(REPOSITORY, get_version()),
        "Source": REPOSITORY,
        "Tracker": "{}/issues".format(REPOSITORY),
    },
    "download_url": "{}/tarball/v{}".format(REPOSITORY, get_version()),
    "packages": find_packages(where=PROJECT, exclude=EXCLUDES),
    "include_package_data": True,
    "package_data": {
        "jupyteranalytics": ["static/*"],
    },
    "data_files": [
        # Automatic `jupyter nbextension install --sys-prefix`
        ("share/jupyter/nbextensions/jupyteranalytics", [
            "jupyteranalytics/static/main.js",
        ]),
        # Automatic `jupyter nbextension enable --sys-prefix`
        ("etc/jupyter/nbconfig/", [
            "jupyter-config/nbconfig/common.json"
        ]),
        #  Automatic `jupyter serverextension enable --sys-prefix`
        ("etc/jupyter/jupyter_notebook_config.d", [
            "jupyter-config/jupyter_notebook_config.d/jupyteranalytics.json"
        ])
    ],
    "zip_safe": False,
    "install_requires": list(get_requires()),
    "python_requires": ">=3.4, <4",
}


##########################################################################
## Run setup script
##########################################################################

if __name__ == '__main__':
    setup(**config)

