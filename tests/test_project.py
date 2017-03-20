import mock
import unittest

from tinypipeline.core import config
from tinypipeline.core.project import Project


class TestProject(unittest.TestCase):

    """Project class."""

    project_name = 'tinypipeline'
    
    print open
    
    @mock.patch('tinypipeline.core.project.open')
    def test_project(self, mocked_open):
        """Initialize a project."""
        project = Project(self.project_name)
        self.assertNotEqual('', project.name)
        self.assertNotEqual('', project.description)
        self.assertNotEqual('', project.template)
        self.assertIn(project.name, str(project))
        self.assertIn(project.description, str(project))
        self.assertIn(project.template, str(project))
    # end def test_project
    
    @mock.patch('tinypipeline.core.project.open')
    @mock.patch('os.path.exists', return_value=True)
    @mock.patch('os.listdir', return_value=['tinypipeline'])
    def test_find_projects(self, listdir, exists, mocked_open):
        """Get all available projects."""
        projects = Project.find_projects()
        self.assertIn(self.project_name, [p.name for p in projects])
    # end def test
# end class TestProject


if __name__ == '__main__':
    unittest.main()
# end if
