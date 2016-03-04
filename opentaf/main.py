"""Entry point to the opentaf engine
"""

import sys
import argparse

from opentaf.signals import SIG_SWITCH
from opentaf.utils.logger import setup_logger
from opentaf.engine.plugger import get_switches, plug

log = setup_logger('opentaf')


def parse_args(argv, switches):
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='switch')
    for switch in switches:
        switch.add_args(subparsers)

    args = parser.parse_args(argv)

    return args


def main(argv):
    # Get the list of available switches
    switches = get_switches()
    # Parse the commandline arguments, including switch args
    args = parse_args(argv, switches)
    # Plug in the required switches depending on the commandline args
    plug(switches, SIG_SWITCH)
    SIG_SWITCH.send(args)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
