# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from uis import Controller
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    app.setStyle(QtGui.QStyleFactory.create('Plastique'))
    main_app = Controller()
    main_app.show()
    sys.exit(app.exec_())






