# jupyteranalytics.extension
# Implements the required notebook and server extension functions.
#
# Author:   PingThings
# Created:  Tue Nov 26 11:54:33 2019 -0500
#
# Copyright (C) 2019 PingThings, Inc.
# For license information, see LICENSE.txt
#
# ID: __init__.py [] benjamin@pingthins.io $

"""
Implements the required notebook and server extension functions.
"""

from notebook.services.config import ConfigManager
from traitlets.config import Configurable
from traitlets import Unicode


CONFIG_SECTION = "common"


__all__ = [
    "_jupyter_server_extension_paths",
    "_jupyter_nbextension_paths",
    "load_jupyter_server_extension",
    "GoogleAnalytics",
    "CONFIG_SECTION",
]


def _jupyter_server_extension_paths():
    """Declare server extensions provided by this package."""
    return [{
        "module": "jupyteranalytics"
    }]


def _jupyter_nbextension_paths():
    """Declare Jupyter extension entry points."""
    return [{
        # Load this on all the pages!
        "section": CONFIG_SECTION,
        # Path relative to the jupyteranalytics directory
        "src": "static",
        # Directory in the nbextension/ namespace
        "dest": "jupyteranalytics",
        # Javascript also in the nbextension/ namespace
        "require": "jupyteranalytics/main"
    }]


def load_jupyter_server_extension(nbapp):
    """Configure and load the extension"""

    # Get the config from the command line if available
    ga = GoogleAnalytics(parent=nbapp)
    ga.setup_config()

    # Check to see if the tracking ID is set
    config = nbapp.config_manager.get(CONFIG_SECTION)
    if config.get("GoogleAnalytics", {}).get("tracking_id", None):
        nbapp.log.info("Google Analytics enabled with Tracking ID")
    else:
        nbapp.log.info("Google Analytics is disabled, no Tracking ID specified")


class GoogleAnalytics(Configurable):
    """
    Configures the Google Analytics Tracking ID from the command line for a single
    session if specified with the --GoogleAnalytics.tracking_id flag.
    """

    tracking_id = Unicode(
        None,
        allow_none=True,
        help="The Google Analytics Tracking ID, usually UA-#########-#.",
        config=True
    )

    def setup_config(self):
        """
        Updates the config for the duration of the user session.
        """
        cm = ConfigManager()
        cm.update(
            CONFIG_SECTION,
            {
                'GoogleAnalytics': {
                    'tracking_id': self.tracking_id
                }
            }
        )
