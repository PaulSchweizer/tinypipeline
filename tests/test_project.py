import mock
import unittest

from tinypipeline.core.project import Project


class TestProject(unittest.TestCase):
    """Project class."""

    project_name = 'tinypipeline'

    @mock.patch('tinypipeline.core.project.Project.open', new_callable=mock.mock_open,
                read_data='{"description": "test", "template": "test"}')
    def test_project(self, mock_open):
        """Initialize a project."""
        project = Project(self.project_name)
        self.assertEqual(project.name, TestProject.project_name)
        self.assertEqual(project.description, 'test')
        self.assertEqual(project.template, 'test')
        self.assertIn(TestProject.project_name, str(project))
        self.assertIn('test', str(project))
    # end def test_project

    @mock.patch('tinypipeline.core.project.Project.open', new_callable=mock.mock_open,
                read_data='{"description": "", "template": ""}')
    @mock.patch('os.path.exists', return_value=True)
    @mock.patch('os.listdir', return_value=['tinypipeline'])
    def test_find_projects(self, listdir, exists, mock_open):
        """Get all available projects."""
        projects = Project.all_projects()
        self.assertIn(self.project_name, [p.name for p in projects])
    # end def test
# end class TestProject


if __name__ == '__main__':
    unittest.main()
# end if
