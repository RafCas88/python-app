import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLineEdit, QPushButton, QProgressBar
from PyQt5.QtCore import Qt


class Downloader(QDialog):
    def __init__(self):
       QDialog.__init__(self)

       layout = QVBoxLayout()

       url = QLineEdit()
       save_location = QLineEdit()
       progress = QProgressBar()
       download = QPushButton("Download")

       url.setPlaceholderText("URL")
       save_location.setPlaceholderText("File save location")

       progress.setValue(0)
       progress.setAlignment(Qt.AlignHCenter)

       layout.addWidget(url)
       layout.addWidget(save_location)
       layout.addWidget(progress)
       layout.addWidget(download)

       self.setLayout(layout)

       self.setWindowTitle("PyDownloader")
       self.setFocus()

app = QApplication(sys.argv)
dl = Downloader()
dl.show()
app.exec_()