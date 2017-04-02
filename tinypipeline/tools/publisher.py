"""Interface for publishing of Asset files."""
from glob import glob
import os
import shutil

from tinypipeline.core import config
from tinypipeline.core.paths import Paths
__all__ = ['IPublisher']


class IPublisher(object):
    """Publish a new version of an Asset."""

    def publish(self, asset, notes):
        """Publish the given asset."""
        next_version = asset.next_version
        if not os.path.exists(os.path.dirname(next_version.path)):
            os.makedirs(os.path.dirname(next_version.path))

        # Save the new version and the corresponding notes
        self.save_file(next_version.path)
        self.save_notes(next_version, notes)

        # Update the latest version and the corresponding notes
        shutil.copy2(next_version.path, asset.latest_version.path)
        shutil.copy2(next_version.notes_file, asset.latest_version.notes_file)
    # end def publish

    def save_notes(self, asset_file, notes):
        """Save the notes next to the asset file."""
        with open(asset_file.notes_file, 'w') as notes_file:
            notes_file.write(notes)
        # end with
    # end def save_notes

    def save_file(self, filepath):
        """Save the file."""
        raise NotImplementedError
    # end def save_file
# end class IPublisher
