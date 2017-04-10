"""Interface for publishing of Asset files."""
from glob import glob
import os
import shutil

from tinypipeline.core import config
from tinypipeline.core.paths import Paths
from tinypipeline.core.asset import Asset
from tinypipeline.core.flow.engine import FlowEngine
from tinypipeline.core.flow.node import FlowNode
from tinypipeline.core.flow.app import FlowApp
__all__ = ['PublisherApp']


class Publish(FlowNode):

    flow_ins = ['asset']
    flow_outs = ['published_file']

    def compute(self):
        # next_version = asset.next_version
        # if not os.path.exists(os.path.dirname(next_version.path)):
        #     os.makedirs(os.path.dirname(next_version.path))

        # # Save the new version and the corresponding notes
        # self.save_file(next_version.path)
        # self.save_notes(next_version, notes)

        # # Update the latest version and the corresponding notes
        # shutil.copy2(next_version.path, asset.latest_version.path)
        # shutil.copy2(next_version.notes_file, asset.latest_version.notes_file)

        self.published_file = self.asset.next_version

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


class NextVersion(FlowNode):

    flow_ins = ['asset']
    flow_outs = ['next_version']

    def compute(self):
        self.next_version = self.asset.next_version


class SaveFile(FlowNode):

    flow_ins = ['asset_file']

    def compute(self):
        self.saved_asset_file = self.asset_file


class SaveNotes(FlowNode):

    flow_ins = ['notes', 'asset_file']

    def compute(self):
        pass


# ---------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------


class PublisherApp(FlowApp):
    """Publish a new version of an Asset."""

    def __init__(self, asset, notes):
        """@todo documentation for __init__."""

        # Build the network
        next_version = NextVersion()
        save_file = SaveFile()
        save_notes = SaveNotes()

        self.nodes = [next_version, save_file, save_notes]

        # Connect the nodes
        next_version.connect('next_version', save_file, 'asset_file')
        next_version.connect('next_version', save_notes, 'asset_file')

        # Set the initial values
        next_version.asset = asset
        save_notes.notes = notes
    # end def __init__
# end class PublisherApp


asset = Asset('MyProject', 'Tiger', 'model')
notes = 'MyNotes'


p_app = PublisherApp(asset, notes)



e = FlowEngine()
e.nodes = p_app.nodes
print e.evaluation_sequence
e.evaluate()




# nv = NextVersion()
# sf = SaveFile()
# sn = SaveNotes()

# nv._asset = asset
# nv.connect(nv.next_version, sf.asset_file)
# nv.connect(nv.next_version, sn.asset_file)
# sn._notes = 'MyNotes'

# e = FlowEngine()
# e.nodes = [nv, sf]

# e.evaluate()

# pn = PublishNode()
# pn._file_to_publish = 'MyFile'

# en = EmailNode()

# rp = RecipientsNode()

# rp.connect(rp.recipients, en.recipients)
# pn.connect(pn.published_file, en.text)


# r = FlowEngine()
# r.nodes = [pn, en, rp]


# r.evaluate()




