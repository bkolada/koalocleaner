# -*- coding: utf-8 -*-

__author__ = 'Kaef'
import zipfile
import shutil
import os

from PyQt4 import QtGui

import WindowErrors as we


def _open_file_selection_window(handler, title='Open File', desc=""):
    fd = QtGui.QFileDialog.getOpenFileName(handler, title, "", desc)
    if fd == "":
        raise we.FileNotSelected()
    return fd

def open_annot_window(handler):
    return _open_file_selection_window(handler, title="Select Kobo Annotation File",
                                       desc='Kobo Annotations File(*.annot)').__str__()


def open_epub_window(handler):
    return _open_file_selection_window(handler, title="Select Correspond Epub File",
                                       desc='Epub File(*.epub)').__str__()


def fill_annotation_table(window_handler, table_handler, annotations):
    table_handler.setRowCount(annotations.annot_num())
    for id, annot in enumerate(annotations.iterate_over_annotations()):
        table_handler.setItem(id, 0, QtGui.QTableWidgetItem(annot[-2]))
        table_handler.setItem(id, 1, QtGui.QTableWidgetItem(annot[0][0]))
        table_handler.setItem(id, 2, QtGui.QTableWidgetItem(("/").join(annot[0][1])))
        table_handler.setItem(id, 3, QtGui.QTableWidgetItem(annot[0][2]))
        table_handler.setItem(id, 4, QtGui.QTableWidgetItem(annot[1][2]))
        table_handler.setItem(id, 5, QtGui.QTableWidgetItem(annot[-1]))


def _clear_entire_temp_folder(path):
    try:
        if os.path.isdir(path):
            shutil.rmtree(path)
            os.mkdir(path)
    except:
        raise we.ClearTemporaryFolderFailed(path)


def unpack_epub(epub_path, dir_path):
    path = os.path.join(dir_path, "tmp_epub", "")
    _clear_entire_temp_folder(path)
    zip = zipfile.ZipFile(epub_path)
    zip.extractall(path)

def get_filename(path):
    a = path.split("/")
    b = path.split("\\")
    if len(a)>len(b):
        return a[-1]
    return b[-1]

def pack_epub(epub_name):
    zip = zipfile.ZipFile("cleared/"+epub_name, 'w', zipfile.ZIP_DEFLATED)
    tg = "tmp_epub/"
    rootlen = len(tg) + 1
    for base, dirs, files in os.walk(tg):
       for file in files:
          fn = os.path.join(base, file)
          zip.write(fn, fn[rootlen:])
    print "aaa"

def get_selected(ctrl):
    return [i.text().__str__() for i in ctrl.selectedItems()]


def set_text_in_ctrl(ctrl, text):
    ctrl.setText("")
    clear_cursor(ctrl)
    ctrl.setText(text)


def get_text_cursor(ctrl):
    return ctrl.textCursor()

def clear_cursor(ctrl):
    cursor = get_text_cursor(ctrl)
    cursor.clearSelection()
    ctrl.setTextCursor(cursor)

def set_text_selection(ctrl, begin, end):
    clear_cursor(ctrl)
    cursor = get_text_cursor(ctrl)
    cursor.setPosition(begin)
    cursor.setPosition(end, QtGui.QTextCursor.KeepAnchor)
    format = QtGui.QTextCharFormat()
    format.setBackground(QtGui.QBrush(QtGui.QColor("green")))
    format.setForeground(QtGui.QBrush(QtGui.QColor("white")))
    cursor.setCharFormat(format)

    ctrl.setTextCursor(cursor)
    ctrl.setFocus()

    cursor = get_text_cursor(ctrl)
    cursor.setPosition(end)
    ctrl.setTextCursor(cursor)