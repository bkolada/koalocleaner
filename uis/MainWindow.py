# -*- coding: utf-8 -*-

import datetime
import os

from PyQt4 import QtGui

from compiled import Ui_MainWindow

class Controller(QtGui.QMainWindow):
    def __init__(self):
        QtGui.QWidget.__init__(self, None)

        self.setup_ui()

    def setup_ui(self):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def connect__buttons(self):
        pass

    def open_epub(self):
        pass

    def open_annot(self):
        pass

    def save_epub(self):
        pass

