"""Sets up the OpenTaf Test Enviroinment
"""

import logging

from opentaf.signals import SIG_SWITCH
from opentaf.plugins import get_plugins, plug
import opentaf.plugins.setup

SETUP_PLUGINS = get_plugins(opentaf.plugins.setup)

log = logging.getLogger('opentaf.switches.setup')


def add_args(parser):
    setup_command = parser.add_parser('setup')
    for plugin in SETUP_PLUGINS:
        plugin.add_args(setup_command)


def connect(args):
    if args.switch == 'setup':
        SIG_SWITCH.connect(setup)


def setup(args):
        # Plug in the required run switch plugins
        plug(SETUP_PLUGINS, args)
