import pkgutil
import argparse

from opentaf.signals import SIG_INIT
import opentaf.plugins


def get_plugins():
    """ Get the list of plugins to be plugged in the opentaf engine
    """
    package = opentaf.plugins
    prefix = package.__name__ + "."
    plugins = list()
    plugin_modules = pkgutil.iter_modules(package.__path__,prefix)
    for importer, modname, ispkg in plugin_modules:
        module = __import__(modname, fromlist="_")
        plugins.append(module)
    return plugins


def plug(plugins):
    for plugin in plugins:
        SIG_INIT.connect(plugin.plug)
