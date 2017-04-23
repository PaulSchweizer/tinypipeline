import os

from maya import cmds

from flowpipe.node import INode
from flowpipe.plug import InputPlug, OutputPlug


class SaveCurrentMayaSceneAs(INode):
    """Save the current Maya scene at the given file path."""

    def __init__(self, name=None):
        """Initialize SaveCurrentMayaSceneAs."""
        super(SaveCurrentMayaSceneAs, self).__init__(name)
        InputPlug('file_path', self)
        OutputPlug('file_path', self)
    # end def __init__

    def compute(self, file_path):
        """Propagate the input value to the output."""
        if not os.path.exists(os.path.dirname(file_path)):
            os.makedirs(os.path.dirname(file_path))
        cmds.file(rn=file_path)
        cmds.file(s=True)
        return {'file_path': file_path}
    # end def compute
# end class SaveCurrentMayaSceneAs


class CurrentAssetNode(INode):

    """Find name, kind and project of current asset in the Maya scene."""

    def __init__(self, name=None):
        """Initialize CurrentAssetNode."""
        super(CurrentAssetNode, self).__init__(name)
        OutputPlug('project', self)
        OutputPlug('name', self)
        OutputPlug('kind', self)
    # end def __init__

    def compute(self):
        """Find the current Asset in the Maya scene."""
        #
        # TODO: Get the information from maya nodes
        #
        return {'project': '__Maya', 'name': 'Tiger', 'kind': 'model'}
    # end def compute
# end class CurrentAssetNode
