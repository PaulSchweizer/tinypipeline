"""Tools to create and query projects."""
import os
import json
import importlib

from tinypipeline.core.paths import Paths
__all__ = ['ProjectCreator']


class ProjectCreator(object):
    """Create the necessary folders on disc for a project."""

    @staticmethod
    def create(name, description, template='base'):
        """Create a new Project on disc."""
        path = Paths.project(project=name)
        if not os.path.exists(path):
            os.makedirs(path)
        # end if

        # The config file
        data = dict(description=description, template=template)
        with open(Paths.project_config(project=name), 'w') as cfg:
            json.dump(data, cfg, indent=4)
        # end with

        # Create the other bootstrap folders, based on the given template
        template = importlib.import_module('project_templates.{0}'
                                           .format(template))
        template.main(name)
    # end def create

    @staticmethod
    def create_path(path):
        """Create the path if necessary."""
        if not os.path.exists(path):
            os.makedirs(path)
        # end if
    # end def create_path
# end class ProjectCreator


if __name__ == '__main__':
    c = ProjectCreator()
    c.create('__MyPyModule', 'MyDescription', 'python')
