from os.path import expanduser
import logging

from opentaf.signals import SIG_INIT
from opentaf.templates import welcome_txt, opentaf_ini, clone

log = logging.getLogger('opentaf.plugins.setupenv')


def add_args(parser):
    pass


def connect(args):
    if args.switch == 'setup':
        SIG_INIT.connect(setup)


def welcome():
    print(welcome_txt.template.template)


def get_input(msg, default=None):
    msgs = [msg]
    msgs.append(': ')
    if default:
        prompt_default = '[DEFAULT: %s](Y/n)? ' % default
        msgs.append(prompt_default)
    print '\n'
    usr_input = raw_input(''.join(msgs)).strip()
    if (default and usr_input == 'n'):
        msgs.remove(prompt_default)
        usr_input = raw_input(''.join(msgs)).strip()
    elif (default and (usr_input.lower() == 'y' or usr_input == '')):
        usr_input = default
    elif not usr_input:
        usr_input = raw_input(''.join(msgs)).strip()
        while not usr_input:
            usr_input = raw_input(''.join(msgs)).strip()

    return usr_input


def setup(args, **kwargs):
    welcome()
    opentaf_root = get_input("OpenTaf Root directory",
                             expanduser('~/'))
    opentaf_testbed = get_input("Testbed to be used for test execution",
                                expanduser('~/testbed.py'))
    test_result_server_ip = get_input("Test result server IP",
                                      "127.0.0.1")
    test_result_server_port = get_input("Test result server port",
                                        "8080")
    scheduler_ip = get_input("Testbed scheduler IP", "127.0.0.1")
    scheduler_port = get_input("Testbed scheduler port", "5672")
    template_values = {
            '__opentaf_root__': opentaf_root,
            '__opentaf_testbed__': opentaf_testbed,
            '__test_result_server_ip__': test_result_server_ip,
            '__test_result_server_port__': test_result_server_port,
            '__testbed_scheduler_ip__': scheduler_ip,
            '__testbed_scheduler__port__': scheduler_port}
    clone(opentaf_ini.template, template_values, expanduser('~/opentaf.ini'))
