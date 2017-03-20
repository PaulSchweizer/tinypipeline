"""Project definition."""
import os
import json

from tinypipeline.core import config
from tinypipeline.core.paths import Paths
__all__ = ['Project']


class Project(object):

    """Representation of a project."""

    def __init__(self, name):
        """Initialize Project."""
        super(Project, self).__init__()
        self.name = name
        self.path = Paths.project(project=name)
        self.config = Paths.project_config(project=name)
        with open(self.config, 'r') as c:
            for attr, value in json.load(c).items():
                setattr(self, attr, value)
            # end for
        # end with
    # end def __init__

    def __str__(self):
        """Pretty string representation."""
        return ('Project:       {self.name}\n'
                'Description:   {self.description}\n'
                'Type:          {self.project_type}\n').format(self=self)
    # end def __str__

    @staticmethod
    def create(name, description, project_type):
        """Create a new Project on disc."""
        path = Paths.project(project=name)
        if os.path.exists(path):
            return
        # end if
        os.makedirs(path)
        data = dict(description=description, project_type=project_type)
        with open(Paths.project_config(project=name), 'w') as c:
            json.dump(data, c, indent=4)
        # end with
    # end def create

    @staticmethod
    def find_projects():
        """Find all available projects."""
        projects = list()
        for name in os.listdir(config.root):
            if os.path.exists(Paths.project_config(project=name)):
                projects.append(Project(name))
            # end if
        # end for
        return projects
    # end def find_projects
# end class Project
