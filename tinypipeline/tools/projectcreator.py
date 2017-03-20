"""Tools to create and query projects."""
import os
import json

from tinypipeline.core.paths import Paths
from tinypipeline.core.project import Project
__all__ = ['ProjectCreator']


class ProjectCreator(object):

    """Create the necessary folders on disc for a project."""

    @staticmethod
    def create(name, description, template):
        """Create a new Project on disc."""
        path = Paths.project(project=name)
        if not os.path.exists(path):
            os.makedirs(path)
        # end if

        data = dict(description=description, template=template)
        with open(Paths.project_config(project=name), 'w') as c:
            json.dump(data, c, indent=4)
        # end with

        # Create the "_unsorted" folder
        ProjectCreator.create_path(Paths.unsorted(project=name))

        # Create the other bootstrap folders, based on the given template
        ProjectCreator.create_python(name)

    # end def create

    @staticmethod
    def create_python(name):
        """Create a folder for python modules in the given Project."""
        ProjectCreator.create_path(Paths.program(project=name,
                                                 program='python'))
    # end def create_python

    @staticmethod
    def create_path(path):
        """Create the path if necessary."""
        if not os.path.exists(path):
            os.makedirs(path)
        # end if
    # end def create_path
# end class ProjectCreator
