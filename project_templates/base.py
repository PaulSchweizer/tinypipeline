import os

from tinypipeline.core.paths import Paths
from tinypipeline.tools.project_creator import ProjectCreator


def main(project):
    ProjectCreator.create_path(Paths.unsorted(project=project))
