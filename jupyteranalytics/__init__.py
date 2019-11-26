# jupyteranalytics
# Adds Google Analytics snippet to Jupyter and JupyterHub
#
# Author:   PingThings
# Created:  Tue Nov 26 11:54:33 2019 -0500
#
# Copyright (C) 2019 PingThings, Inc.
# For license information, see LICENSE.txt
#
# ID: __init__.py [] benjamin@pingthins.io $

"""
Adds Google Analytics snippet to Jupyter and JupyterHub
"""

##########################################################################
## Imports
##########################################################################

from .extension import *
from .version import get_version


##########################################################################
## Version
##########################################################################

__version__ = get_version()