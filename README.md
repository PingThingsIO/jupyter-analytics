# Jupyter Analytics

A simple Jupyter Notebook extension to inject [Google Analytics](https://www.google.com/analytics/) tracking code into notebooks and JupyterHub web pages. This extension is based on [yuvipanda/nbgoogleanyltics](https://github.com/yuvipanda/nbgoogleanalytics) but is extended for larger JupyterHub deployments.

## Installation

Install the extension as follows:

```
$ pip install jupyteranalytics
```

This should both install and enable the `jupyteranalytics` extension. Verify with:

```
$ jupyter nbextension list
$ jupyter serverextension list
```

There are a couple of reasons why this might not have been installed and enabled automagically. If not, you can manually install and enable as follows:

```
$ jupyter nbextension install --py --sys-prefix jupyteranalytics
$ jupyter nbextension enable --py --sys-prefix jupyteranalytics
$ jupyter serverextension enable --py --sys-prefix jupyteranalytics
```

Note that both the automatic and manual methods install `jupyteranalytics` to your virtualenv using the `--sys-prefix` flag by default. Alternatively you can omit this flag or specify `--user` to install the configuration to your user configuration or you can use `--system` to install the extension systemwide.

**Warning**: For Google Analytics tracking to appear on every page (including the directory listing), the configuration must be in `nbconfig/common.json`, the pip installer will copy a new configuration to the virtualenv location; ensure that you make a backup of any existing `nbconfig.common.json` file. Note that this will not affect user or system installs, which require manual enabling of the extension.

## Configuration

The configuration property required by this extension is a Google Analytics Tracking ID, which can be obtained after you set up a Google Analytics property. This ID looks something like `UA-#########-#`.

To quickly get started you can pass this id as a command line parameter:

```
$ jupyter notebook --GoogleAnalytics.tracking_id="UA-#########-#"
```

To permenantly enable tracking on all notebook pages, check the path to your configuration using `jupyter nbextension list`. Then, in `<config_path>/common.json` add the following:

```json
{
    "GoogleAnalytics": {
        "tracking_id": "UA-#########-#"
    }
}
```

Alternatively you can set the Trackig ID by storing it in the `GOOGLE_ANALYTICS_TRACKING_ID` environment variable, this is particularly useful if you're deploying JupyterHub with Docker or Kubernetes.

Note that the notebook logger will indicate if tracking is enabled if it can find the Tracking ID from the configuration, the environment, or the command line (resolved in that order). It will also indicate if the analytics are disabled because no tracking id could be found. Ensure that you have system logging enabled to check that your deployment is correct.
