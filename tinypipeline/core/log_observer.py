"""Push log messages to observer for redistribution.

Allows to easily pipe logs and messages to a UI.
"""


class LogObserver(object):

    """@todo documentation for LogObserver."""

    listeners = list()

    message = ''

    @staticmethod
    def push(message):
        """@todo documentation"""
        LogObserver.message = message
        LogObserver.inform_listeners()
    # end def push

    @staticmethod
    def inform_listeners():
        """@todo documentation"""
        for listener in LogObserver.listeners:
            listener(LogObserver.message)
        # end for
    # end def inform_listeners
# end class LogObserver
