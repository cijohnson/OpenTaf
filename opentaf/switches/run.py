"""Executes the testcases or testsuite
"""

import logging

from engine import OpenTafEngine
from opentaf.signals import SIG_INIT
from opentaf.engine.plugger import get_plugins, plug
import opentaf.plugins.run

RUN_PLUGINS = get_plugins(opentaf.plugins.run)

log = logging.getLogger('opentaf.switches.run')


def add_args(parser):
    run_command = parser.add_parser('run')
    run_command.add_argument('-t', '--testcase', dest='testcases',
                             help='List of testcases to be executed')
    run_command.add_argument('-T', '--testsuite', dest='testsuite',
                             help='Testsuite to be executed')
    for plugin in RUN_PLUGINS:
        plugin.add_args(run_command)


def connect(args):
    if args.switch == 'run':
        # Plug in the required run switch plugins
        plug(RUN_PLUGINS, SIG_INIT)
        SIG_INIT.send(args)
        # Start the test execution engine
        engine = OpenTafEngine(args)
        engine.start()
