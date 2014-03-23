# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtGui
from uis import Controller
import sys
import os
import signal
signal.signal(signal.SIGINT, signal.SIG_DFL)

if __name__ == '__main__':
    sys.path.append(os.path.join(os.path.dirname(__file__)))
    app = QtGui.QApplication(sys.argv)
    app.setStyle(QtGui.QStyleFactory.create('Plastique'))
    main_app = Controller(os.path.join(os.path.dirname(__file__)))
    main_app.show()
    sys.exit(app.exec_())






