import os
import datetime
import logging

__all__ = ['setup_logger']

LOG_DIR = os.path.expanduser('~/opentaf/logs/')


def setup_logger(rootname='opentaf'):
    """Root logger for the opentaf.
    """
    log = logging.getLogger(rootname)
    log.setLevel(logging.DEBUG)
    # create file handler which logs even debug messages
    fh = logging.FileHandler(gen_log_filename())
    fh.setLevel(logging.DEBUG)
    # create console handler with a higher log level
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    # create formatter and add it to the handlers
    formatter = logging.Formatter(
        '[%(asctime)s %(name)s(%(lineno)s) %(levelname)s]: %(message)s',
        datefmt='%a %b %d %H:%M:%S %Y')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)
    # add the handlers to the logger
    log.addHandler(fh)
    log.addHandler(ch)

    return log


def gen_log_filename(prefix='opentaf'):
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
    ts = datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S_%f")
    return '%s/%s-%s.log' % (LOG_DIR, prefix, ts)
