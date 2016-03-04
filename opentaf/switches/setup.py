"""Sets up the OpenTaf Test Enviroinment
"""

import logging

from opentaf.signals import SIG_INIT
from opentaf.engine.plugger import get_plugins, plug
import opentaf.plugins.setup

SETUP_PLUGINS = get_plugins(opentaf.plugins.setup)

log = logging.getLogger('opentaf.switches.setup')


def add_args(parser):
    setup_command = parser.add_parser('setup')
    setup_command.add_argument('-i', '--opentaf-input', default='PROMPT',
                               help='Input INI file to opentaf')
    for plugin in SETUP_PLUGINS:
        plugin.add_args(setup_command)


def connect(args):
    if args.switch == 'setup':
        # Plug in the required run switch plugins
        plug(SETUP_PLUGINS, SIG_INIT)
        SIG_INIT.send(args)
