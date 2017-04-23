from __future__ import print_function

from flowpipe.node import INode
from flowpipe.plug import InputPlug, OutputPlug

from tinypipeline.core.asset import Asset


class AssetNode(INode):
    """Holding an Asset."""

    def __init__(self, name=None):
        """Init the node."""
        super(AssetNode, self).__init__(name)
        InputPlug('project', self)
        InputPlug('name', self)
        InputPlug('kind', self)

        OutputPlug('asset', self)
        OutputPlug('next_version', self)
        OutputPlug('next_version_notes', self)
        OutputPlug('latest_version', self)
        OutputPlug('latest_version_notes', self)
    # end def __init__

    def compute(self, project, name, kind):
        """Propagate the input value to the output."""
        asset = Asset(project, name, kind)
        return {'asset': asset,
                'next_version': asset.next_version.path,
                'next_version_notes': asset.next_version.notes_file,
                'latest_version': asset.latest_version.path,
                'latest_version_notes': asset.latest_version.notes_file}
    # end def compute
# end class AssetNode
