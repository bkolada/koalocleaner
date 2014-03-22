# -*- coding: utf-8 -*-

import datetime
import os

from PyQt4 import QtGui

from compiled import Ui_MainWindow
from handlers import AnnotationHandler
import WindowErrors as we
import SupportingFunctions as sf

class Controller(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QWidget.__init__(self, None)
        self.setup_ui()
        self.clear_fields()

    def clear_fields(self):
        self.annot_handler = AnnotationHandler()


    def setup_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_buttons()

    def connect_buttons(self):
        self.ui.open_annot.clicked.connect(self.open_annot)
        self.ui.open_epub.clicked.connect(self.open_epub)

    def open_epub(self):
        pass

    def open_annot(self):
        try:
            file = sf.open_annot_window(self)
            self.log(file)
            self.annot_handler
        except we.FileNotSelected as msg:
            self.log(msg)

    def save_epub(self):
        pass

    def log(self, log):
        print log