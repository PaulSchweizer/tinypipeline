import sys
if sys.version_info[0] < 3:
    import __builtin__
    open_patch = '__builtin__.open'
else:
    import builtins
    open_patch = 'builtins.open'
import mock
import unittest

from tinypipeline.core.project import Project


class TestProject(unittest.TestCase):
    """Project class."""

    project_name = 'tinypipeline'

    @mock.patch('os.path.exists', return_value=True)
    @mock.patch(open_patch, new_callable=mock.mock_open,
                read_data='{"description": "test", "template": "test"}')
    def test_project(self, mock_open, exists):
        """Initialize a project."""
        prj = Project(self.project_name)
        self.assertEqual(prj.name, TestProject.project_name)
        self.assertEqual(prj.description, 'test')
        self.assertEqual(prj.template, 'test')
        self.assertIn(TestProject.project_name, str(prj))
        self.assertIn('test', str(prj))
    # end def test_project

    @mock.patch(open_patch, new_callable=mock.mock_open,
                read_data='{"description": "", "template": ""}')
    @mock.patch('os.path.exists', return_value=True)
    @mock.patch('os.listdir', return_value=['tinypipeline'])
    def test_find_projects(self, listdir, exists, mock_open):
        """Get all available projects."""
        projects = Project.all_projects()
        self.assertIn(self.project_name, [p.name for p in projects])
    # end def test

    def test_current_project(self):
        """Set and get the current project from the env var."""
        project = Project(self.project_name)

        self.assertNotEqual(project.name, Project.current().name)

        project.set_as_current()
        self.assertEqual(project.name, Project.current().name)
    # end def test_current_project
# end class TestProject


if __name__ == '__main__':
    unittest.main()
# end if
