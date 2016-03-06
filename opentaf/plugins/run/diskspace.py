import os
import logging

from opentaf.signals import SIG_PRERUN
from opentaf.exceptions import CriticalError

THRESHOLD = 98
WARN_THRESHOLD = 90

log = logging.getLogger('opentaf.plugins.diskspace')


def add_args(parser):
    parser.add_argument("--enable-disk-check", action="store_true",
                        help="Enables disk space check")


def connect(args):
    if args.enable_disk_check:
        SIG_PRERUN.connect(check_diskspace)


def check_diskspace(sender, **kwargs):
    import pdb; pdb.set_trace()
    log.info("Checking disk space.")
    use_percentage = get_disk_usage('~/')
    if use_percentage >= THRESHOLD:
        raise CriticalError("Disk is %s full" % use_percentage)
    elif use_percentage >= WARN_THRESHOLD:
        log.warning("Disk usage: %s is almost reached threshold: %s",
                    use_percentage, THRESHOLD)
    else:
        log.info("Sufficent disk space available")


def get_disk_usage(location):
    s = os.statvfs(os.path.expanduser(location))
    total = s.f_blocks * s.f_bsize
    free = s.f_bavail * s.f_frsize
    used = total - free
    return (used / float(total)) * 100
