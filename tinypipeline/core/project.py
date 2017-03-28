"""Project definition."""
import os
import json

from tinypipeline.core import config
from tinypipeline.core.paths import Paths
__all__ = ['Project']


class Project(object):
    """Representation of a project."""

    def __init__(self, name):
        """Initialize the Project by the given name.

        Add the information from the config file, if possible.
        Args:
            name (str): The (unique) name of the project
        """
        super(Project, self).__init__()
        self.name = name
        self.description = ''
        self.template = ''

        project_config = Paths.project_config(project=name)
        if os.path.exists(project_config):
            with open(project_config, 'r') as cfg:
                for attr, value in json.load(cfg).items():
                    setattr(self, attr, value)
                # end for
            # end with
        # end if
    # end def __init__

    def __str__(self):
        """Pretty string representation."""
        return ('Project:       {self.name}\n'
                'Description:   {self.description}\n'
                'Template:      {self.template}\n').format(self=self)
    # end def __str__

    @staticmethod
    def all_projects():
        """Find all available projects."""
        projects = list()
        for name in os.listdir(config.root):
            if os.path.exists(Paths.project_config(project=name)):
                projects.append(Project(name))
            # end if
        # end for
        return projects
    # end def all_projects
# end class Project
