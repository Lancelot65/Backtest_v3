from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.showMaximized()
        self.setWindowTitle('Backtest')

app = QApplication(sys.argv)

w = Window()
w.show()
app.exec()