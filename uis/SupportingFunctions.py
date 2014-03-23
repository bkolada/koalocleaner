# -*- coding: utf-8 -*-

__author__ = 'Kaef'
from PyQt4 import QtGui
import WindowErrors as we
import zipfile
import shutil
import os

def _open_file_selection_window(handler, title='Open File', desc=""):
    fd = QtGui.QFileDialog.getOpenFileName(handler, title, "",desc)
    if fd == "":
        raise we.FileNotSelected()
    return fd

def open_annot_window(handler):
    return _open_file_selection_window(handler, title="Select Kobo Annotation File",
                                       desc= 'Kobo Annotations File(*.annot)').__str__()

def open_epub_window(handler):
    return _open_file_selection_window(handler, title="Select Correspond Epub File",
                                       desc= 'Epub File(*.epub)').__str__()

def fill_annotation_table(window_handler, table_handler, annotations):
    table_handler.setRowCount(annotations.annot_num())
    for id,annot in enumerate(annotations.iterate_over_annotations()):
        table_handler.setItem(id, 0, QtGui.QTableWidgetItem(annot[-2]))
        table_handler.setItem(id, 1, QtGui.QTableWidgetItem(annot[0][0]))
        table_handler.setItem(id, 2, QtGui.QTableWidgetItem(("/").join(annot[0][1])))
        table_handler.setItem(id, 3, QtGui.QTableWidgetItem(annot[0][2]))
        table_handler.setItem(id, 4, QtGui.QTableWidgetItem(annot[1][2]))
        table_handler.setItem(id, 5, QtGui.QTableWidgetItem(annot[-1]))

def _clear_entire_temp_folder(path):
    try:
        shutil.rmtree(path)
        os.mkdir(path)
    except:
        raise we.ClearTemporaryFolderFailed(path)

def unpack_epub(epub_path, dir_path):
    path =  os.path.join(dir_path,"tmp_epub","")
    _clear_entire_temp_folder(path)
    zip = zipfile.ZipFile(epub_path)
    zip.extractall(path)