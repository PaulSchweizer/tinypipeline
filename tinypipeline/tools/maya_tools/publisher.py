"""Publisher for Maya Asset files."""
from maya import cmds

from tinypipeline.tools.publisher import IPublisher
__all__ = ['MayaPublisher']


class MayaPublisher(IPublisher):
    """Publish Maya files for Assets."""

    def save_file(self, filepath):
        """Publish the given asset."""
        cmds.file(rn=filepath)
        cmds.file(s=True)
    # end def save_file
# end class MayaPublisher
