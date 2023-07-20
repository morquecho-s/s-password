from PySide6.QtWidgets import QWidget
from PySide6.QtCore import (QRect,QSize, Qt,Signal)
from PySide6.QtGui import (QCursor)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,QPushButton, QSizePolicy, QWidget)
from backend.conection import conect

class Frame(QWidget):
    isDeleted = Signal()
    def __init__(self,email:str = "example email",password:str = "example password",id:int = None,group:str="none")->None:
        super().__init__()
        self.frame = QFrame(self)
        self.setObjectName(u"frame")
        self.setGeometry(QRect(-60, 160, 477, 150))
        self.setMaximumSize(QSize(16777215, 150))
        # self.setFrameShape(QFrame.StyledPanel)
        # self.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel()
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.horizontalLayout_2.addWidget(self.label)

        self.label_2 = QLabel()
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.label3 = QLabel()
        self.label3.setObjectName(u"label_3")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label3.sizePolicy().hasHeightForWidth())
        self.label3.setSizePolicy(sizePolicy)
        self.label3.setAlignment(Qt.AlignCenter)
        self.label3.setWordWrap(True)
        self.label3.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.horizontalLayout_2.addWidget(self.label3)


        self.boton = QPushButton()
        self.boton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(1)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.boton.sizePolicy().hasHeightForWidth())
        self.boton.setSizePolicy(sizePolicy1)
        self.boton.setCursor(QCursor(Qt.PointingHandCursor))
        self.horizontalLayout_2.addWidget(self.boton)
        self.boton.setText("Borrar")
        self.setLayout(self.horizontalLayout_2)


        #! propiedades
        self.__email:str = email
        self.__password:str = password
        self.__id:int = id
        self.__group:str = group
        self.setEmail(self.__email)
        self.setPassword(self.__password)
        self.setGroup(self.__group)
        self.__init_events()

    def __init_events(self)->None:
        self.boton.clicked.connect(self.__delete_frame)

    def setEmail(self, email:str)->None:
        self.label.setText(email)
        self.__email = email

    def setPassword(self,password:str)->None:
        self.label_2.setText(password)
        self.__password = password

    def setGroup(self,group:str)->None:
        self.label3.setText(group)
        self.__group = group

    def __delete_frame(self)->None:
        request = conect.template_request.copy()
        request[conect.HEAD][conect.TYPE] = conect.DELETE
        request[conect.CONTENT][conect.EMAIL] = self.__email
        request[conect.CONTENT][conect.PASSWORD] = self.__password
        request[conect.CONTENT][conect.GROUP] = self.__group
        if not self.__id == None:
            request[conect.CONTENT][conect.ID] = str(self.__id)
        conect.request(request)
        self.isDeleted.emit()


if __name__ == "__main__":
    app = QApplication()
    a = Frame()
    a.show()
    app.exec()