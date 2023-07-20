try:
    from ui.pre_window import Ui_Form
    from tools import objects
    from backend.conection import conect
except:
    from pre_window import Ui_Form
    from ..tools import objects

from PySide6.QtWidgets import QWidget,QMainWindow,QApplication,QDialog,QHBoxLayout,QLineEdit,QPushButton,QMessageBox
from tkinter.filedialog import askdirectory

import re

class MainWindow(QMainWindow):
    def __init__(self)->None:
        super().__init__()
        self._ui = Ui_Form()
        temp_widget = QWidget()
        self._ui.setupUi(temp_widget)
        self.setCentralWidget(temp_widget)
        self.__init_events()
        self.load_frames()
        self.__lock_frames()

    def __init_events(self)->None:
        self._ui.pushButton_2.clicked.connect(self.add_frame)
        self._ui.botonActualizar.clicked.connect(self.__restart_window)
        self._ui.botonExportar.clicked.connect(self.__export_frames_to_html)
        self._ui.button_login.clicked.connect(lambda:self.__check_magic_word(self._ui.linePasword.text()))
        self._ui.button_login.setShortcut("Ctrl+Space")

    def __lock_frames(self)->None:
        self._ui.right_container.setVisible(False)
        self.__change_aspect_line(self._ui.linePasword,False)

    def __unlock_frames(self):
        self._ui.right_container.setVisible(True)
        self.__change_aspect_line(self._ui.linePasword,True)

    def __check_magic_word(self,word:str)->bool:
        if "sarahi" in word.lower() or word.lower() == "alz":
            self.__unlock_frames()
            self._ui.linePasword.setText("")
            self._ui.linePasword.setPlaceholderText("-.-")
        else:
            self.__lock_frames()

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
        modal = QDialog(self)
        modal.setMinimumSize(500,100)
        layout = QHBoxLayout(modal)
        boton = QPushButton("aceptar",modal)
        line_email = QLineEdit(modal)
        line_email.setPlaceholderText("tu correo electrónico:")
        line_email.textChanged.connect(lambda:self.__validate_lines_modal(line_email,line_password,boton))
        line_password = QLineEdit(modal)
        line_password.setPlaceholderText("tu contraseña:(min.7 caracteres)")
        line_password.textChanged.connect(lambda:self.__validate_lines_modal(line_email,line_password,boton))
        line_group = QLineEdit(modal)
        line_group.setPlaceholderText("tu grupo:")
        self.__change_aspect_line(line_group,True)
        layout.addWidget(line_email)
        layout.addWidget(line_password)
        layout.addWidget(line_group)
        layout.addWidget(boton)
        boton.clicked.connect(lambda:modal.accept())
        self.__validate_lines_modal(line_email,line_password,boton)
        return (modal.exec(),line_email.text(),line_password.text(),line_group.text())
        
    def add_frame(self)->None:
        its_ok,email,password,group = self.__show_modal()
        if its_ok:
            if len(group.replace(' ','')) == 0:
                group = "none"
            request = conect.template_request.copy()
            request[conect.HEAD][conect.TYPE] = conect.POST
            request[conect.CONTENT][conect.PASSWORD] = password
            request[conect.CONTENT][conect.EMAIL] = email
            request[conect.CONTENT][conect.GROUP] = group
            conect.request(request)
            new_frame = objects.Frame(email,password,None,group)
            self.__add_frame_to_screen(new_frame)

    def __add_frame_to_screen(self, frame:objects.Frame)->bool:
        try:
            frame.isDeleted.connect(self.__restart_window)
            self._ui.verticalLayout_4.addWidget(frame)
            return True
        except Exception as e:
            print(e)
            return False

    def load_frames(self)->None:
        request = conect.template_request.copy()
        request[conect.HEAD][conect.TYPE] = conect.GET
        request[conect.CONTENT][conect.PASSWORD] = ""
        request[conect.CONTENT][conect.EMAIL] = ""
        request[conect.CONTENT][conect.GROUP] = ""
        result = conect.request(request)
        if len(result) > 0 and isinstance(result,list):
            for frame_data in result:
                self.__add_frame_to_screen(objects.Frame(frame_data[0],frame_data[1],frame_data[3],frame_data[2]))

    def __restart_window(self)->None:
        for i in range(self._ui.verticalLayout_4.count()):
            item = self._ui.verticalLayout_4.itemAt(0)
            widget = item.widget()
            if widget is not None:
                self._ui.verticalLayout_4.removeWidget(widget)
                widget.deleteLater()
        
        self.load_frames()
       

    def __export_frames_to_html(self)->None:
        dir_to_export = askdirectory(title="Donde guardaras la tabla??")
        if len(dir_to_export) > 0:
            
            request = conect.template_request.copy()
            request[conect.HEAD][conect.TYPE] = conect.EXPORT
            request[conect.HEAD][conect.DIR_TO_EXPORT] = dir_to_export
            conect.request(request)
        else:
            QMessageBox.critical(self,"Error de ruta!","Necesitas seleccionar una ruta para poder guardar tu tabla correctamente...")
            
            







# relleno para llegar a la linea 150:> 