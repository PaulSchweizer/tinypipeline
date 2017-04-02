"""Asset definition."""
import glob
import os

from tinypipeline.core import config
from tinypipeline.core.paths import Paths
from tinypipeline.core.project import Project
__all__ = ['Asset', 'AssetFile']


class Asset(object):
    """Representation of an asset."""

    def __init__(self, project, name, kind):
        """Initialize the Asset by the given name.

        Args:
            project (Project): Project this Asset belongs to.
            name (str): The (unique) name of the asset.
        """
        super(Asset, self).__init__()
        if isinstance(project, basestring):
            self.project = Project(project)
        else:
            self.project = project
        # end if
        self.name = name
        self.kind = kind
    # end def __init__

    def __str__(self):
        """Pretty string representation."""
        return ('{self.name} ({self.kind}, {self.project.name})'
                .format(self=self))
    # end def __str__

    @property
    def workfiles(self):
        """All work files of this Asset."""
        path = Paths.step(project=self.project.name, name=self.name,
                          kind=self.kind, step='work')
        if not os.path.exists(path):
            return list()
        else:
            pattern = Paths.asset_work(project=self.project.name,
                                       name=self.name, kind=self.kind,
                                       version='*', ext=config.maya_ext)
            return [AssetFile(f) for f in sorted(glob.glob(pattern))]
    # end def workfiles

    @property
    def versions(self):
        """All published files of this Asset."""
        path = Paths.step(project=self.project.name, name=self.name,
                          kind=self.kind, step='published')

        if not os.path.exists(path):
            return list()
        else:
            pattern = Paths.asset_published(project=self.project.name,
                                            name=self.name, kind=self.kind,
                                            version='*', ext=config.maya_ext)
            return [AssetFile(f) for f in sorted(glob.glob(pattern))]
    # end def versions

    @property
    def latest_version(self):
        """The latest_version published file of this Asset."""
        filepath = Paths.asset_latest(project=self.project.name,
                                      name=self.name, kind=self.kind,
                                      ext=config.maya_ext)
        if not os.path.exists(filepath):
            return None
        else:
            return AssetFile(filepath)
    # end def latest_version

    @property
    def next_version(self):
        """The next publish file of this Asset."""
        next_version = '{0:0>{padding}}'.format(len(self.versions) + 1,
                                                padding=config.padding)
        return AssetFile(Paths.asset_published(project=self.project.name,
                                               name=self.name,
                                               kind=self.kind,
                                               version=next_version,
                                               ext=config.maya_ext))
    # end def next_version
# end class Asset


class AssetFile(object):
    """Containing the file path and the notes."""

    def __init__(self, path):
        """Retrieve the notes corresponding to this file."""
        super(AssetFile, self).__init__()
        self.path = path
        self.notes = ''
        self.notes_file = Paths.notes(path=os.path.dirname(path),
                                      filename=os.path.basename(path))
        # Get the notes from file if possible
        if os.path.exists(self.notes_file):
            with open(self.notes_file, 'r') as notes:
                self.notes = notes.read()
            # end with
        # end if
    # end def __init__

    def __str__(self):
        """Pretty string representation."""
        return ('{self.path}\n    "{self.notes}"'.format(self=self))
    # end def __str__
# end class AssetFile
