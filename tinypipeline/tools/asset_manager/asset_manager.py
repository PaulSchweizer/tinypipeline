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
        self.update_projects_list()
        self.new_btn.clicked.connect(self.new_project)
        self.projects_lst.itemClicked.connect(self.show_project_details)
        self.splitter.setSizes([150, self.width()-150])
        self.filter_led.textChanged.connect(self.update_projects_list)
    # end def __init__

    def update_projects_list(self):
        """Show all projects."""
        self.projects_lst.clear()
        f = self.filter_led.text()
        projects = [p for p in Project.all_projects() if f in p.name]
        for project in projects:
            self.projects_lst.addItem(project.name)
        # end for
    # end def update_projects_list

    def new_project(self):
        """Create a new project."""
        dialog = CreateProjectDialog(self)
        dialog.setWindowFlags(QtCore.Qt.Widget |
                              QtCore.Qt.FramelessWindowHint |
                              QtCore.Qt.Popup)
        w = dialog.width()
        h = dialog.height()
        pos = self.mapToGlobal(self.new_btn.pos())
        x = pos.x()
        y = pos.y() + 32 + 9
        dialog.setGeometry(x, y, w, h)
        dialog.create_btn.clicked.connect(self.update_projects_list)
        dialog.show()
    # end def new_project

    def show_project_details(self, item):
        """Display the details of the selected project."""
        project = Project(item.text())
        self.name_lbl.setText(project.name)
        self.description_lbl.setText(project.description)
        self.template_lbl.setText(project.template)
    # end def show_project_details
# end class AssetManager


class CreateProjectDialog(utility.ui_class(__file__, 'CreateProjectDialog')):
    """Create a new project."""

    def __init__(self, parent=None):
        """Initialize CreateProjectDialog."""
        super(CreateProjectDialog, self).__init__(parent=parent)
        self.template_cbx.addItems(ProjectCreator.templates())
        self.name_led.textChanged.connect(self.update_path)
        self.create_btn.clicked.connect(self.create)
        self.update_path('')
    # end def __init__

    def update_path(self, text):
        """Update the path display."""
        self.path_lbl.setText(Paths.project(project=text))
    # end def update_path

    def create(self):
        """Create a new project."""
        name = self.name_led.text()
        description = self.description_led.text()
        template = self.template_cbx.currentText()
        try:
            ProjectCreator.create(name, description, template)
            self.close()
        except Exception as error:
            print error
        # end try
    # end def create
# end class CreateProjectDialog


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    man = AssetManager()
    man.show()
    sys.exit(app.exec_())
