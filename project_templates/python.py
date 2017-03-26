import os

from tinypipeline.core.paths import Paths
from tinypipeline.tools.project_creator import ProjectCreator


def main(project):
    py_path = Paths.program(project=project, program=project)
    ProjectCreator.create_path(py_path)
    with open(os.path.join(py_path, '__init__.py'), 'w'):
        pass
    with open(os.path.join(py_path, '{}.py'.format(project)), 'w'):
        pass

    tests = Paths.program(project=project, program='tests')
    ProjectCreator.create_path(tests)
    with open(os.path.join(tests, '__init__.py'), 'w'):
        pass
