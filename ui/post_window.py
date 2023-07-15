try:
    from ui.pre_window import Ui_Form
except:
    from pre_window import Ui_Form

from PySide6.QtWidgets import QWidget,QMainWindow,QApplication

class MainWindow(QMainWindow):
    def __init__(self)->None:
        super().__init__()
        self._ui = Ui_Form()
        a = QWidget()
        self._ui.setupUi(a)
        self.setCentralWidget(a)
        self.show()

app = QApplication()
x =MainWindow()


app.exec()