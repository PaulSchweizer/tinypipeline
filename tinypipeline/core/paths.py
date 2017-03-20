"""Map paths based on patterns defined in the config file."""
import os
from functools import partial

from tinypipeline.core import config


class Paths(object):

    """Handle paths within the pipeline."""

    def __getattr__(self, attr):
        """Get the path behind the given attr pattern."""
        if attr in config.patterns.keys():
            return partial(Paths.get, attr)
        else:
            raise AttributeError('Invalid pattern \'{0}\'. {1}'.format(attr,
                                                                   str(self)))
        # end if
    # end def __getattr__

    @staticmethod
    def get(*args, **kwargs):
        """Get a path from the given arguments.

        Returns:
            The path
        """
        return os.path.join(config.root,
                            config.patterns[args[0]].format(**kwargs))
    # end def get

    def __str__(self):
        """All available patterns."""
        return ('Available patterns:\n\t{0}'
                .format('\n\t'.join(['{0}: {1}'.format(k, v)
                                     for k, v in config.patterns.items()])))
    # end def __str__
# end class paths


Paths = Paths()
