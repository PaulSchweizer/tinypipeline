from __future__ import print_function

import os

from flowpipe.node import INode
from flowpipe.plug import InputPlug, OutputPlug

from tinypipeline.core import config


class EnvNode(INode):
    """Holding an Asset."""

    def __init__(self, name=None):
        """Init the node."""
        super(EnvNode, self).__init__(name)
        for env_var in config.env_vars:
            OutputPlug(env_var, self)
    # end def __init__

    def compute(self):
        """Retrieve all relevant environment variables."""
        env = dict()
        for env_var in config.env_vars:
            if env_var in os.environ:
                env[env_var] = os.environ[env_var]
            else:
                env[env_var] = None
        return env
    # end def compute
# end class EnvNode
