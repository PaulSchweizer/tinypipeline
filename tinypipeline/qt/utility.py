"""Useful qt utility functions."""
import os
import xml.etree.ElementTree as xml
from cStringIO import StringIO

import pysideuic
from Qt import QtWidgets


def ui_class(widget_file, widget_name):
    """Build a class from a designer .ui file."""
    b, f = _load_ui_type(get_ui_file_path(widget_file, widget_name))
    class BaseUi(b, f):
        def __init__(self, parent=None):
            super(BaseUi, self).__init__(parent=parent)
            self.setupUi(self)
    return BaseUi
# end def ui_class


def _load_ui_type(ui_file):
    """Load a ui file for PySide.

    PySide lacks the "_load_ui_type" command, so we have to convert
    the UI file to python code in-memory first and then execute it in a
    special frame to retrieve the form_class.
    Args:
        ui_file (str): The .ui file.
    Returns:
        The base and form class, derived from the .ui file.
    """
    parsed = xml.parse(ui_file)
    widget_class = parsed.find('widget').get('class')
    form_class = parsed.find('class').text
    with open(ui_file, 'r') as f:
        o = StringIO()
        frame = {}

        pysideuic.compileUi(f, o, indent=0)
        pyc = compile(o.getvalue(), '<string>', 'exec')
        exec pyc in frame

        # Fetch the base_class and form_class based on their type
        # in the xml from designer
        base_class = getattr(QtWidgets, widget_class)
        form_class = frame['Ui_%s' % form_class]
        return base_class, form_class
    # end reading the ui file
# end def _load_ui_type


def get_ui_file_path(widget_file, widget_name):
    """Retrieve the ui file for the given widget.

    It is assumed that it is set up inside the standardized
    resource folder.
    Args:
        widget_file (str): The file path to the widget code.
        widget_name (str): The class name of the widget.
    Returns:
        The file path for the ui file.
    """
    return os.path.join(os.path.dirname(widget_file),
                        'resource', '%s.ui' % widget_name)
# end def get_ui_file_path


def get_css_file_path(widget_file, widget_name):
    """Retrieve the stylesheet file for the given widget.

    It is assumed that it is set up inside the standardized
    resource folder.
    Args:
        widget_file (str): The file path to the widget code.
        widget_name (str): The class name of the widget.
    Returns:
        The file path for the stylesheet file.
    """
    return os.path.join(os.path.dirname(widget_file),
                        'resource', '%s.css' % widget_name)
# end def get_css_file_path


def set_stylesheet(widget, widget_file=None):
    """Set the style sheet to the given widget.

    The general stylesheet and an additional stylesheet for
    the given widget are merged.
    For this to work, the widget has to come with a resource folder on
    the same folder level and a .css file named like the class name.
    Args:
        widget (QWidget): The widget.
        widget_file (str): Optional file path of the widget.
    """
    general_css_file = os.path.join(os.path.dirname(__file__),
                                    'resource', 'general.css')
    with open(general_css_file, 'r') as f:
        general_css = f.read()
    # end reading the general css file

    if widget_file is not None:
        widget_css_file = get_css_file_path(widget_file,
                                            widget.__class__.__name__)
        if os.path.exists(widget_css_file):
            with open(widget_css_file, 'r') as f:
                widget_css = f.read()
            # end reading the widget's css file
            general_css += widget_css
        # end if
    # end if
    widget.setStyleSheet(general_css)
# end def set_stylesheet
