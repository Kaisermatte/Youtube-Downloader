from PyQt6 import QtWidgets, QtGui
from Window import Ui_Main_window
import yt_dlownload


class MainWindow(QtWidgets.QMainWindow, Ui_Main_window):
    # Constructor für Gui von MainWindow
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        # Fortschrittbalken initialisieren
        self.progressBar.setValue(0)

        self.btn_start_mp4.clicked.connect(lambda: yt_dlownload.download_yt_video(self.input_url.text(), 'bestvideo[height<=2160][ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best', self.update_progress))
        self.btn_start_mp3.clicked.connect(lambda: yt_dlownload.download_yt_video(self.input_url.text(), 'bestaudio', self.update_progress))
        self.btn_exit.clicked.connect(lambda: exit())

    def update_progress(self, percent):
        print(f"Fortschritt: {percent}%")  # Debugging
        self.progressBar.setValue(percent)
        QtWidgets.QApplication.processEvents()  # UI-Update erzwingen