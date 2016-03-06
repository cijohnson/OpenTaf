"""Entry point to the opentaf engine
"""

import sys
import argparse

from opentaf.utils.logger import setup_logger
from opentaf.switches import get_switches, on_switch

log = setup_logger('opentaf')


def parse_args(argv, switches):
    parser = argparse.ArgumentParser()
    parser.add_argument('-I', '--input-ini', default='~/opentaf.ini',
                        help='Input INI file for this test run')
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
    # Switch on the required switches depending on the commandline args
    on_switch(switches, args)

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
