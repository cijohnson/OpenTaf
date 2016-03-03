""" Signals used by opentaf.
"""

from blinker import signal


# First signal emitted by opentaf, when trigered
# This is a internally used signal.
# Example: plug callback in all plugins are connected to this signal
SIG_INIT = signal('INIT')


# Emitted before test suite execution
# all pre testsuite plugins should be connected to this signal
SIG_PRERUN = signal('PRERUN')


# Emitted after test suite execution
# all post testsuite plugins should be connected to this signal
SIG_POSTRUN = signal('POSTRUN')


# Emitted before each testcase execution
# all pre test plugins should be connected to this signal
SIG_PRETEST = signal('PRETEST')


# Emitted after each testcase execution
# all post test plugins should be connected to this signal
SIG_POSTTEST = signal('POSTTEST')


# Last signal emitted by opentaf before exiting the test run
SIG_DONE = signal('DONE')
