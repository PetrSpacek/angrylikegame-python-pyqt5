import sys
from PyQt5.QtWidgets import QApplication

from app_window.qt import QtAppWindow

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QtAppWindow()
    window.show()

    # Set timer for regular time ticks
    window.start_timer()

    # Wrapping the GUI execution into `sys.exit()` to ensure that proper result code
    # will be returned when the window closes (otherwise it's always 0)
    #sys.exit(app.exec_())
    app.exec()