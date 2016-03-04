import pkgutil
import opentaf.switches


def get_plugins(package):
    """ Get the list of plugins to be plugged in the opentaf engine switches
    """
    prefix = package.__name__ + "."
    plugins = list()
    plugin_modules = pkgutil.iter_modules(package.__path__, prefix)
    for importer, modname, ispkg in plugin_modules:
        module = __import__(modname, fromlist="_")
        plugins.append(module)
    return plugins


def get_switches():
    """ Get the list of switches to be plugged in the opentaf engine
    """
    return get_plugins(opentaf.switches)


def plug(plugins, signal):
    for plugin in plugins:
        signal.connect(plugin.connect)
