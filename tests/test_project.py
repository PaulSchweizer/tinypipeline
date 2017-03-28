import __builtin__
import mock
import unittest

from tinypipeline.core import project


class TestProject(unittest.TestCase):
    """Project class."""

    project_name = 'tinypipeline'
    
    @mock.patch('os.path.exists', return_value=True)
    @mock.patch('__builtin__.open', new_callable=mock.mock_open,
                read_data='{"description": "test", "template": "test"}')
    def test_project(self, mock_open, exists):
        """Initialize a project."""
        prj = project.Project(self.project_name)
        self.assertEqual(prj.name, TestProject.project_name)
        self.assertEqual(prj.description, 'test')
        self.assertEqual(prj.template, 'test')
        self.assertIn(TestProject.project_name, str(prj))
        self.assertIn('test', str(prj))
    # end def test_project

    @mock.patch('__builtin__.open', new_callable=mock.mock_open,
                read_data='{"description": "", "template": ""}')
    @mock.patch('os.path.exists', return_value=True)
    @mock.patch('os.listdir', return_value=['tinypipeline'])
    def test_find_projects(self, listdir, exists, mock_open):
        """Get all available projects."""
        projects = project.Project.all_projects()
        self.assertIn(self.project_name, [p.name for p in projects])
    # end def test
# end class TestProject


if __name__ == '__main__':
    unittest.main()
# end if
