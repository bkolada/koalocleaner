# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_TEM.ui'
#
# Created: Sun Apr 06 23:25:46 2014
#      by: PyQt4 UI code generator 4.8.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1043, 608)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.widget_8 = QtGui.QWidget(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_8.sizePolicy().hasHeightForWidth())
        self.widget_8.setSizePolicy(sizePolicy)
        self.widget_8.setObjectName(_fromUtf8("widget_8"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.widget_8)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.widget_5 = QtGui.QWidget(self.widget_8)
        self.widget_5.setObjectName(_fromUtf8("widget_5"))
        self.gridLayout = QtGui.QGridLayout(self.widget_5)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.open_epub = QtGui.QPushButton(self.widget_5)
        self.open_epub.setObjectName(_fromUtf8("open_epub"))
        self.gridLayout.addWidget(self.open_epub, 0, 1, 1, 1)
        self.open_annot = QtGui.QPushButton(self.widget_5)
        self.open_annot.setObjectName(_fromUtf8("open_annot"))
        self.gridLayout.addWidget(self.open_annot, 0, 0, 1, 1)
        self.save_epub = QtGui.QPushButton(self.widget_5)
        self.save_epub.setObjectName(_fromUtf8("save_epub"))
        self.gridLayout.addWidget(self.save_epub, 0, 2, 1, 1)
        self.verticalLayout_4.addWidget(self.widget_5)
        self.widget_2 = QtGui.QWidget(self.widget_8)
        self.widget_2.setObjectName(_fromUtf8("widget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setMargin(0)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.widget_6 = QtGui.QWidget(self.widget_2)
        self.widget_6.setObjectName(_fromUtf8("widget_6"))
        self.gridLayout_2 = QtGui.QGridLayout(self.widget_6)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.label_4 = QtGui.QLabel(self.widget_6)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.annot_table = QtGui.QTableWidget(self.widget_6)
        self.annot_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.annot_table.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.annot_table.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.annot_table.setObjectName(_fromUtf8("annot_table"))
        self.annot_table.setColumnCount(6)
        self.annot_table.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.annot_table.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.annot_table.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.annot_table.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.annot_table.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.annot_table.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.annot_table.setHorizontalHeaderItem(5, item)
        self.annot_table.horizontalHeader().setStretchLastSection(True)
        self.gridLayout_2.addWidget(self.annot_table, 1, 0, 1, 1)
        self.horizontalLayout_2.addWidget(self.widget_6)
        self.verticalLayout_4.addWidget(self.widget_2)
        self.load = QtGui.QPushButton(self.widget_8)
        self.load.setObjectName(_fromUtf8("load"))
        self.verticalLayout_4.addWidget(self.load)
        self.widget_4 = QtGui.QWidget(self.widget_8)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
        self.widget_4.setObjectName(_fromUtf8("widget_4"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.widget_4)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.widget = QtGui.QWidget(self.widget_4)
        self.widget.setObjectName(_fromUtf8("widget"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.widget)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout_2.addWidget(self.label)
        self.before = QtGui.QTextEdit(self.widget)
        self.before.setEnabled(False)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.before.setFont(font)
        self.before.setObjectName(_fromUtf8("before"))
        self.verticalLayout_2.addWidget(self.before)
        self.horizontalLayout.addWidget(self.widget)
        self.widget_3 = QtGui.QWidget(self.widget_4)
        self.widget_3.setObjectName(_fromUtf8("widget_3"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.widget_3)
        self.verticalLayout_3.setMargin(0)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.label_3 = QtGui.QLabel(self.widget_3)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout_3.addWidget(self.label_3)
        self.after = QtGui.QTextEdit(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.after.setFont(font)
        self.after.setObjectName(_fromUtf8("after"))
        self.verticalLayout_3.addWidget(self.after)
        self.horizontalLayout.addWidget(self.widget_3)
        self.verticalLayout_4.addWidget(self.widget_4)
        self.widget_7 = QtGui.QWidget(self.widget_8)
        self.widget_7.setObjectName(_fromUtf8("widget_7"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.widget_7)
        self.horizontalLayout_4.setMargin(0)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.save_paragraph_changes = QtGui.QPushButton(self.widget_7)
        self.save_paragraph_changes.setObjectName(_fromUtf8("save_paragraph_changes"))
        self.horizontalLayout_4.addWidget(self.save_paragraph_changes)
        self.verticalLayout_4.addWidget(self.widget_7)
        self.horizontalLayout_3.addWidget(self.widget_8)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.plainTextEdit_3 = QtGui.QPlainTextEdit(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit_3.sizePolicy().hasHeightForWidth())
        self.plainTextEdit_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lucida Console"))
        font.setPointSize(7)
        self.plainTextEdit_3.setFont(font)
        self.plainTextEdit_3.setObjectName(_fromUtf8("plainTextEdit_3"))
        self.verticalLayout.addWidget(self.plainTextEdit_3)
        self.horizontalLayout_3.addWidget(self.groupBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Th3 3p4b M4s73r", None, QtGui.QApplication.UnicodeUTF8))
        self.open_epub.setText(QtGui.QApplication.translate("MainWindow", "Open epub", None, QtGui.QApplication.UnicodeUTF8))
        self.open_annot.setText(QtGui.QApplication.translate("MainWindow", "Open annotations", None, QtGui.QApplication.UnicodeUTF8))
        self.save_epub.setText(QtGui.QApplication.translate("MainWindow", "Save changes", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Available annotations", None, QtGui.QApplication.UnicodeUTF8))
        self.annot_table.setSortingEnabled(True)
        self.annot_table.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("MainWindow", "Annotation", None, QtGui.QApplication.UnicodeUTF8))
        self.annot_table.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.annot_table.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("MainWindow", "Start par", None, QtGui.QApplication.UnicodeUTF8))
        self.annot_table.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("MainWindow", "Start pos", None, QtGui.QApplication.UnicodeUTF8))
        self.annot_table.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("MainWindow", "End pos", None, QtGui.QApplication.UnicodeUTF8))
        self.annot_table.horizontalHeaderItem(5).setText(QtGui.QApplication.translate("MainWindow", "Comment", None, QtGui.QApplication.UnicodeUTF8))
        self.load.setText(QtGui.QApplication.translate("MainWindow", "Load", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Paragraph before", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Paragraph after", None, QtGui.QApplication.UnicodeUTF8))
        self.save_paragraph_changes.setText(QtGui.QApplication.translate("MainWindow", "Save changes in paragraph", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("MainWindow", "Logger", None, QtGui.QApplication.UnicodeUTF8))

