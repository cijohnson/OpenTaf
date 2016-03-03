""" Core Test Executing engine
"""

from opentaf.signals import (SIG_PRERUN, SIG_POSTRUN, SIG_PRETEST,
                             SIG_POSTTEST, SIG_DONE)


class OpenTafEngine(object):
    def __init__(self, args):
        self.args = args

    def start(self):
        SIG_PRERUN.send()
        # for suite in testsuite:
        #     Emit PRERUN signal to trigger pre-testsuite plugins
        #     SIG_PRERUN.send()
        #         for test in suite or testcases:
        #         SIG_PRETEST.send()
        #         Execute test
        #         SIG_POSTTEST.send()
        #     Emit POSTRUN signal to trigger pre-testsuite plugins
        #     SIG_POSTRUN.send()
        # Emit DONE signal for internal plugins
        SIG_DONE.send()
