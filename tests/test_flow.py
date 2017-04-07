""""""
from tinypipeline.core.flow.node import FlowNode, flow_out, flow_in
from tinypipeline.core.flow.engine import FlowEngine


class PublishNode(FlowNode):
    """@todo documentation for PublishNode."""

    @flow_out
    def published_file(self):
        """@todo documentation for published_file."""
        return self._published_file
    # end def published_file

    def compute(self):
        """@todo documentation for compute."""
        print 'Computing', self.__class__.__name__
        self._published_file = 'MyPublishedFile'
    # end def compute
# end class PublishNode


class EmailNode(FlowNode):
    """@todo documentation for EmailNode."""

    @flow_in
    def text(self, value):
        """@todo documentation for text."""
        self._text = value
    # end def text

    @flow_in
    def recipients(self, value):
        """@todo documentation for recipients."""
        self._recipients = value
    # end def recipients

    def compute(self):
        """@todo documentation for compute."""
        print 'Sending an email to: ', self._recipients, 'with text:' ,self._text
    # end def compute
# end class EmailNode


class RecipientsNode(FlowNode):
    """@todo documentation for RecipientsNode."""

    _recipients = list()

    @flow_out
    def recipients(self):
        """@todo documentation for recipients."""
        return self._recipients
    # end def recipients

    def compute(self):
        """@todo documentation for compute."""
        print 'Setting the recipients.'
        self._recipients = ['Me', 'You', 'Her']
    # end def compute
# end class RecipientsNode


# ---------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------


pn = PublishNode()
pn._file_to_publish = 'MyFile'

en = EmailNode()

rp = RecipientsNode()

rp.connect(rp.recipients, en.recipients)
pn.connect(pn.published_file, en.text)


r = FlowEngine()
r.nodes = [pn, en, rp]


r.evaluate()




# ---------------------------------------------------------------------
# This fails, need to reorder the sequence
# ---------------------------------------------------------------------



"""Interface for publishing of Asset files."""
from glob import glob
import os
import shutil

from tinypipeline.core import config
from tinypipeline.core.paths import Paths
from tinypipeline.core.asset import Asset
from tinypipeline.core.flow.engine import FlowEngine
from tinypipeline.core.flow.node import FlowNode, flow_in, flow_out
__all__ = ['IPublisher']


class IPublisher(FlowNode):
    """Publish a new version of an Asset."""

    @flow_out
    def published_file(self):
        """@todo documentation for published_file."""
        return self._published_file
    # end def published_file

    def compute(self, asset, notes):
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

        self._published_file = next_version
    # end def compute

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


# asset -> NextVersion -> SaveFile  -> publish
# notes -> ----------- -> save_notes -> publish


class NextVersion(FlowNode):

    @flow_in
    def asset(self, value):
        self._asset = value

    @flow_out
    def next_version(self):
        return self._next_version

    def compute(self):
        self._next_version = self._asset.next_version


class SaveFile(FlowNode):

    @flow_in
    def asset_file(self, value):
        self._asset_file = value

    @flow_out
    def saved_asset_file(self):
        return self._saved_asset_file

    def compute(self):
        self._saved_asset_file = self._asset_file


class SaveNotes(FlowNode):

    @flow_in
    def notes(self, value):
        self._notes = value

    @flow_in
    def asset_file(self, value):
        self._asset_file = value

    @flow_out
    def saved_notes_file(self):
        return self._saved_notes_file

    def compute(self):
        self._saved_notes_file = self._asset_file.notes_file


# ---------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------


asset = Asset('MyProject', 'Tiger', 'model')


nv = NextVersion()
sf = SaveFile()
sn = SaveNotes()

nv._asset = asset
nv.connect(nv.next_version, sf.asset_file)
nv.connect(nv.next_version, sn.asset_file)
sn._notes = 'MyNotes'

e = FlowEngine()
e.nodes = [nv, sf]

e.evaluate()

# pn = PublishNode()
# pn._file_to_publish = 'MyFile'

# en = EmailNode()

# rp = RecipientsNode()

# rp.connect(rp.recipients, en.recipients)
# pn.connect(pn.published_file, en.text)


# r = FlowEngine()
# r.nodes = [pn, en, rp]


# r.evaluate()















