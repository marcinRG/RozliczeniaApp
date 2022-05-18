from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class MGWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 600, 600)
        self.setWindowTitle('Jakieś okienko')
        self.show()


