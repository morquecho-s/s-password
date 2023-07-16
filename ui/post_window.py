try:
    from ui.pre_window import Ui_Form
    from tools import objects
except:
    from pre_window import Ui_Form
    from ..tools import objects

from PySide6.QtWidgets import QWidget,QMainWindow,QApplication

class MainWindow(QMainWindow):
    def __init__(self)->None:
        super().__init__()
        self._ui = Ui_Form()
        temp_widget = QWidget()
        self._ui.setupUi(temp_widget)
        self.setCentralWidget(temp_widget)
        self.__init_events()

    def __init_events(self)->None:
        self._ui.pushButton_2.clicked.connect(self.add_frame)

    def add_frame(self)->None:
        self._ui.verticalLayout_4.addWidget(objects.Frame())

if __name__ == '__main__':
    app = QApplication()
    x = MainWindow()
    x.show()
    app.exec()