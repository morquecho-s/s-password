try:
    from ui.pre_window import Ui_Form
    from tools import objects
except:
    from pre_window import Ui_Form
    from ..tools import objects

from PySide6.QtWidgets import QWidget,QMainWindow,QApplication,QDialog,QHBoxLayout,QLineEdit,QPushButton
import re

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

    def __change_aspect_line(self,lineEdit:QLineEdit,its_ok:bool)->None:
        if its_ok:
            color = "green"
        else:
            color = "red"
        lineEdit.setStyleSheet("""
                                QLineEdit{
                                    border:2px solid """+f"{color}" +""";
                                }
                                """)

    def validate_email(self,email:str,line_edit:QLineEdit)->bool:
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if re.match(patron, email):
        
            returned = True
        else:
        
            returned = False
        self.__change_aspect_line(line_edit,returned)
        return returned
    
    def validate_password(self, password:str,line_edit:QLineEdit)->bool:
        if len(password) >= 7:
            returned = True
        else:
            returned = False

        self.__change_aspect_line(line_edit,returned)
        return returned
    
    
    def __validate_lines_modal(self,line1:QLineEdit,line2:QLineEdit,boton:QPushButton)->None:
        line1_ok = self.validate_email(line1.text(),line1) 
        line2_ok = self.validate_password(line2.text(),line2)
        
        if line1_ok and line2_ok:
            boton.setEnabled(True)
        else:
            boton.setEnabled(False)

    def __show_modal(self)->None:
        # Creando las modal
        def accept_modal()->None:
            return (modal.exec(),line_email.text(),line_password.text())

        modal = QDialog(self)
        modal.setBaseSize(400,200)
        layout = QHBoxLayout(modal)
        boton = QPushButton(modal,"aceptar")
        line_email = QLineEdit(modal)
        line_email.textChanged.connect(lambda:self.__validate_lines_modal(line_email,line_password,boton))
        line_password = QLineEdit(modal)
        line_password.textChanged.connect(lambda:self.__validate_lines_modal(line_email,line_password,boton))
        layout.addWidget(line_email)
        layout.addWidget(line_password)
        layout.addWidget(boton)
        boton.clicked.connect(lambda:modal.accept())
        self.__validate_lines_modal(line_email,line_password,boton)

        return (modal.exec(),line_email.text(),line_password.text())
        

    
    def add_frame(self)->None:
        its_ok,email,password = self.__show_modal()
        if its_ok:
            self._ui.verticalLayout_4.addWidget(objects.Frame(email,password))
        

if __name__ == '__main__':
    app = QApplication()
    x = MainWindow()
    x.show()
    app.exec()