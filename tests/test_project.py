import mock
import os
import unittest

from tinypipeline.core import config
from tinypipeline.core.project import Project


class TestProject(unittest.TestCase):

    """@todo documentation for TestProject."""

    project = 'tinypipeline'

    @mock.patch('__main__.open')
    def test_project(self, open_mock):
        """@todo documentation for test_project."""
        project = Project(self.project)

        self.assertNotEqual('', project.name)
        self.assertNotEqual('', project.path)
        self.assertNotEqual('', project.description)
        self.assertNotEqual('', project.project_type)
        self.assertIn(project.name, project.__str__())
        self.assertIn(project.description, project.__str__())
        self.assertIn(project.project_type, project.__str__())
    # end def test_project

    @mock.patch('__main__.open')
    @mock.patch('os.path.exists', return_value=True)
    @mock.patch('os.listdir', return_value=['tinypipeline'])
    def test_find_projects(self, listdir, exists, open_mock):
        """@todo documentation for test."""
        projects = Project.find_projects()
        self.assertIn(self.project, [p.name for p in projects])
    # end def test
# end class TestProject


if __name__ == '__main__':
    unittest.main()
# end if
