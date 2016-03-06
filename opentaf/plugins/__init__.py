import pkgutil

from opentaf.signals import SIG_INIT


def get_plugins(package):
    """ Get the list of plugins
    """
    prefix = package.__name__ + "."
    plugins = list()
    plugin_modules = pkgutil.iter_modules(package.__path__, prefix)
    for importer, modname, ispkg in plugin_modules:
        module = __import__(modname, fromlist="_")
        plugins.append(module)
    return plugins


def plug(plugins, args=None):
    """Plugs the plugins to the swtiches
    """
    for plugin in plugins:
        plugin.connect(args)
    if args:
        SIG_INIT.send(args)
    else:
        SIG_INIT.send()
