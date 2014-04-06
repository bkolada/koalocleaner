# -*- coding: utf-8 -*-

import datetime
import os

from PyQt4 import QtGui

from compiled import Ui_MainWindow
from handlers import AnnotationHandler, EpubParser, EpubExport
import WindowErrors as we
import SupportingFunctions as sf

class Controller(QtGui.QMainWindow):
    def __init__(self, main_path):
        QtGui.QWidget.__init__(self, None)
        self.main_path = main_path
        self.setup_ui()
        self.clear_fields()
        self.filename = None

    def clear_fields(self):
        self.annot_handler = AnnotationHandler()
        self.epub_container = EpubParser()

    def setup_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_buttons()

    def connect_buttons(self):
        self.ui.open_annot.clicked.connect(self.open_annot)
        self.ui.open_epub.clicked.connect(self.open_epub)
        self.ui.load.clicked.connect(self.load_selected_annotation)
        self.ui.save_paragraph_changes.clicked.connect(self.save_paragraph_changes)
        self.ui.save_epub.clicked.connect(self.save_epub)

    def open_epub(self):
        try:
            file = sf.open_epub_window(self)
            self.log(file)
            sf.unpack_epub(file,self.main_path)
            self.filename = sf.get_filename(file)
            self.setWindowTitle(self.filename)
            self.log("File loaded")
        except we.FileNotSelected as msg:
            self.log(msg)


    def open_annot(self):
        try:
            file = sf.open_annot_window(self)
            self.log(file)
            self.annot_handler.parse_xml(file)
            sf.fill_annotation_table(self, self.ui.annot_table, self.annot_handler)
        except we.FileNotSelected as msg:
            self.log(msg)

    def load_selected_annotation(self):
        annot = sf.get_selected(self.ui.annot_table)
        container = self.epub_container.parse(os.path.join("tmp_epub",annot[1]))
        path = [int(i) for i in annot[2].split("/")[2:]]
        print container.get_content(path)[int(annot[3]):int(annot[4])]
        text = container.get_content(path)
        sf.set_text_in_ctrl(self.ui.before, text)
        sf.set_text_in_ctrl(self.ui.after, text)
        sf.set_text_selection(self.ui.after,int(annot[3]),int(annot[4]))

    def save_paragraph_changes(self):
        text = self.ui.after.toPlainText().__str__()
        annot = sf.get_selected(self.ui.annot_table)
        container = self.epub_container.parse(os.path.join("tmp_epub",annot[1]))
        path = [int(i) for i in annot[2].split("/")[2:]]
        container.set_content(path,text)
        ee = EpubExport()
        ee.export_container_to_file(os.path.join("tmp_epub",annot[1]), container)

    def save_epub(self):
        sf.pack_epub(self.filename)

    def log(self, log):
        print log