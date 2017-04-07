"""UI to create and browse projects."""
from Qt import QtCore, QtWidgets

from tinypipeline.qt import utility
from tinypipeline.core.paths import Paths
from tinypipeline.core.project import Project
from tinypipeline.tools.project_creator import ProjectCreator
__all__ = ['AssetManager']


class AssetManager(utility.ui_class(__file__, 'AssetManager')):
    """UI to create and browse projects."""

    def __init__(self):
        """Initialize widgets and signals."""
        super(AssetManager, self).__init__()
    # end def __init__
# end class AssetManager


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    man = AssetManager()
    man.show()
    sys.exit(app.exec_())
