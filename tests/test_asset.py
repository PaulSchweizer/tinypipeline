import sys

if sys.version_info[0] < 3:
    import __builtin__
    open_patch = '__builtin__.open'
else:
    import builtins
    open_patch = 'builtins.open'

import os
import re
import unittest
import mock

from tinypipeline.core.asset import Asset, AssetFile
from tinypipeline.core.project import Project
from tinypipeline.core.paths import Paths
from tinypipeline.core import config


class TestAsset(unittest.TestCase):
    """Test the Asset classes."""

    def test_init(self):
        """Provide Project as string and Project object."""
        asset_a = Asset('TestProject', 'AssetName', 'AssetKind')
        asset_b = Asset(Project('TestProject'), 'AssetName', 'AssetKind')
        self.assertEqual(str(asset_a), str(asset_b))
    # end def test_init

    @mock.patch(open_patch, new_callable=mock.mock_open, read_data='Some Notes')
    @mock.patch('glob.glob')
    @mock.patch('os.path.exists', return_value=False)
    def test_workfile(self, exists, glob, mock_open):
        """Retrieve all workfiles."""
        asset = Asset('TestProject', 'AssetName', 'AssetKind')

        self.assertEqual(0, len(asset.workfiles))

        # 12 Workfiles exist
        exists.return_value = True
        glob.return_value = [Paths.asset_work(project=asset.project.name,
                                              name=asset.name, kind=asset.kind,
                                              version='{0:0>{padding}}'.format(i, padding=config.padding),
                                              ext=config.maya_ext) for i in range(1, 13)]
        self.assertEqual(12, len(asset.workfiles))
    # end def test_workfile

    @mock.patch(open_patch, new_callable=mock.mock_open, read_data='Some Notes')
    @mock.patch('glob.glob')
    @mock.patch('os.path.exists', return_value=False)
    def test_versions(self, exists, glob, mock_open):
        """Retrieve all published versions."""
        asset = Asset('TestProject', 'AssetName', 'AssetKind')

        self.assertEqual(0, len(asset.versions))

        # 12 Versions exist
        exists.return_value = True
        glob.return_value = [Paths.asset_published(project=asset.project.name,
                                                   name=asset.name, kind=asset.kind,
                                                   version='{0:0>{padding}}'.format(i, padding=config.padding),
                                                   ext=config.maya_ext) for i in range(1, 13)]
        self.assertEqual(12, len(asset.versions))
    # end def test_versions

    @mock.patch(open_patch, new_callable=mock.mock_open, read_data='Some Notes')
    @mock.patch('os.path.exists', return_value=False)
    def test_latest(self, exists, mock_open):
        """Retrieve the latest published version."""
        asset = Asset('TestProject', 'AssetName', 'AssetKind')

        self.assertIsNone(asset.latest_version)

        # A latest version exists
        exists.return_value = True
        self.assertIsNotNone(asset.latest_version)
    # end def test_latest

    @mock.patch(open_patch, new_callable=mock.mock_open, read_data='Some Notes')
    @mock.patch('glob.glob')
    @mock.patch('os.path.exists', return_value=False)
    def test_next_version(self, exists, glob, mock_open):
        """Retrieve the next version to publish."""
        asset = Asset('TestProject', 'AssetName', 'AssetKind')

        # No version exists yet
        self.assertEqual(0, len(asset.versions))

        self.assertEqual(Paths.asset_published(project=asset.project.name,
                                               name=asset.name,
                                               kind=asset.kind,
                                               version='{0:0>{padding}}'.format(1, padding=config.padding),
                                               ext=config.maya_ext),
                         asset.next_version.path)

        # Next Version is 12th Version
        exists.return_value = True
        glob.return_value = [Paths.asset_published(project=asset.project.name,
                                                   name=asset.name, kind=asset.kind,
                                                   version='{0:0>{padding}}'.format(i, padding=config.padding),
                                                   ext=config.maya_ext) for i in range(1, 12)]
        self.assertEqual(Paths.asset_published(project=asset.project.name,
                                               name=asset.name,
                                               kind=asset.kind,
                                               version='{0:0>{padding}}'.format(12, padding=config.padding),
                                               ext=config.maya_ext),
                         asset.next_version.path)
    # end def test_next_version

    @mock.patch(open_patch, new_callable=mock.mock_open, read_data='Some Notes')
    @mock.patch('os.path.exists', return_value=True)
    def test_asset_file(self, exists, mock_open):
        """AssetFile contains the path, notes and path to the notes."""
        path = Paths.asset_published(project='TestProject',
                                     name='AssetName',
                                     kind='AssetKind',
                                     version='{0:0>{padding}}'.format(12, padding=config.padding),
                                     ext=config.maya_ext)
        notes_file = Paths.notes(path=os.path.dirname(path),
                                      filename=os.path.basename(path))

        af = AssetFile(path)
        self.assertEqual(path, af.path)
        self.assertEqual('Some Notes', af.notes)
        self.assertEqual(notes_file, af.notes_file)
        self.assertIn(path, str(af))
        self.assertIn('Some Notes', str(af))
    # end def test_asset_file
# end class TestAsset


if __name__ == '__main__':
    unittest.main()
# end if
