
import opentaf.switches
from opentaf.signals import SIG_SWITCH
from opentaf.plugins import get_plugins


def get_switches():
    """ Get the list of switches to be connected to  opentaf engine
    """
    return get_plugins(opentaf.switches)


def on_switch(switches=None, args=None):
    """Connects the switches to opentaf
    """
    for switch in switches or get_switches():
        switch.connect(args)
    if args:
        SIG_SWITCH.send(args)
    else:
        SIG_SWITCH.send()
