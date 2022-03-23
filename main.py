from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QApplication, QLineEdit, QPushButton


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('To jest jakiś tekst')

        # self.show()
        self.setLayout(QVBoxLayout())

        my_label = QLabel('To jest jakiś tekst')
        my_text = QLineEdit()
        my_text.setText('')
        my_button = QPushButton('Naciśnij')

        self.layout().addWidget(my_label)
        self.layout().addWidget(my_text)
        self.layout().addWidget(my_button)
        self.show()


app = QApplication([])
my_window = MyWindow()

app.exec_()
