import sys

from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem

from forms.tableView import *
from db_cms.db_cms_core import DbCMS


# class MyForm(QDialog):
#     def __init__(self):
#         super().__init__()
#         self.ui = Ui_Dialog()
#         self.ui.setupUi(self)
#         self.ui.changeNameBtn.clicked.connect(self.change_name)
#         self.ui.closeBtn.clicked.connect(self.close_app)
#         self.show()
#
#     def change_name(self):
#         name = self.ui.nameLineInput.text()
#         self.ui.labelName.setText(name)
#
#     def close_app(self):
#         self.close()


class MyTableView(QWidget):
    my_db = None

    def __init__(self):
        self.my_db = DbCMS('sqlite:///resources/db/app_data.db')
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.fill_table()
        self.show()

    def fill_table(self):

        data = self.my_db.show_all_tax_rate()
        for indexRow, row in enumerate(data):
            self.ui.tableWidget.insertRow(indexRow)
            for indexCol, item in enumerate(row):
                if indexRow == 0:
                    self.ui.tableWidget.insertColumn(indexCol)
                elem = QTableWidgetItem(str(item))
                self.ui.tableWidget.setItem(indexRow, indexCol, elem)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MyTableView()
    w.show()
    sys.exit(app.exec_())
