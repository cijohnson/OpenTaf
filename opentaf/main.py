"""Entry point to the opentaf engine
"""

import sys
import logging
import argparse

from engine import OpenTafEngine
from opentaf.signals import SIG_INIT
from opentaf.utils.logger import setup_logger
from opentaf.engine.plugger import get_plugins, plug

log = setup_logger('opentaf')


def parse_args(argv, plugins):
    parser = argparse.ArgumentParser()
    for plugin in plugins:
        plugin.add_args(parser)

    args = parser.parse_args(argv)

    return args


def main(argv):
    # Get the list of available plugins
    plugins = get_plugins()
    # Parse the commandline arguments, including plugin args
    args = parse_args(argv, plugins)
    # Plug in the required plugins depending on the commandline args
    plug(plugins)
    SIG_INIT.send(args)
    # Start the test execution engine
    engine = OpenTafEngine(args)
    engine.start()

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
