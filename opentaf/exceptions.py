"""OpenTaf exception definitions.
"""


class OpenTafException(Exception):
     def __str__(self, msg):
         return 'opentaf: %s' % (str(msg))


class CriticalError(OpenTafException):
    pass
