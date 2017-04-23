"""Nodes for writing and reading data."""
from __future__ import print_function

import os
import shutil

from flowpipe.node import INode
from flowpipe.plug import InputPlug, OutputPlug


class WriteTextToFileNode(INode):
    """Save the text to a file."""

    def __init__(self, name=None):
        """Initialize WriteTextToFileNode."""
        super(WriteTextToFileNode, self).__init__(name)
        InputPlug('text', self)
        InputPlug('file_path', self)
        OutputPlug('text', self)
        OutputPlug('file_path', self)
    # end def __init__

    def compute(self, text, file_path):
        """Save the text to the given file."""
        if not os.path.exists(os.path.dirname(file_path)):
            os.makedirs(os.path.dirname(file_path))
        with open(file_path, 'w') as text_file:
            text_file.write(text)
        return {'text': text,
                'file_path': file_path}
    # end def compute
# end class WriteTextToFileNode


class CopyFileNode(INode):
    """Copy the source file to the destination."""

    def __init__(self, name=None):
        """Initialize CopyFileNode."""
        super(CopyFileNode, self).__init__(name)
        InputPlug('source', self)
        InputPlug('destination', self)
    # end def __init__

    def compute(self, source, destination):
        """Copy the file."""
        shutil.copy2(source, destination)
    # end def compute
# end class CopyFileNode
