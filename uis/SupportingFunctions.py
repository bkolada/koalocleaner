# -*- coding: utf-8 -*-

__author__ = 'Kaef'
from PyQt4 import QtGui
import WindowErrors as we

def _open_file_selection_window(handler, title='Open File', desc=""):
    fd = QtGui.QFileDialog.getOpenFileName(handler, title, "",desc)
    if fd == "":
        raise we.FileNotSelected()
    return fd

def open_annot_window(handler):
    return _open_file_selection_window(handler, title="Select Kobo Annotation File",
                                       desc= 'Kobo Annotations File(*.annot)')

def open_epub_window(handler):
    return _open_file_selection_window(handler, title="Select Correspond Epub File",
                                       desc= 'Epub File(*.epub)')

