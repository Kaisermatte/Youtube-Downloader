import sys

from PyQt6.QtGui import QIcon
from MainWindow import MainWindow
from PyQt6 import QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.setWindowIcon(QIcon('download24.ico'))
    main_window.show()
    sys.exit(app.exec())
