
from PySide6.QtCore import (QCoreApplication, 
    QMetaObject, QRect,
    QSize, Qt)
from PySide6.QtGui import  QCursor,QFont
from PySide6.QtWidgets import (QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 600)
        Form.setStyleSheet(u"*{\n"
"color:#2c2c2c;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #eee;\n"
"}\n"
"QPushButton{\n"
"	background-color:qlineargradient(spread:pad, x1:0.890273, y1:1, x2:0.2105, y2:0.057, stop:0 rgba(75, 225, 22, 255), stop:1 rgba(165, 255, 134, 255));\n"
"	padding:10px;\n"
"	border-radius:10px;\n"
"	border:3px solid transparent;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:transparent;\n"
"	border-color:rgba(165, 255, 134, 255);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgba(165, 255, 134, 255);\n"
"	border-color:transparent;\n"
"}")
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.left_container = QFrame(Form)
        self.left_container.setObjectName(u"left_container")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.left_container.sizePolicy().hasHeightForWidth())
        self.left_container.setSizePolicy(sizePolicy)
        self.left_container.setMaximumSize(QSize(500, 16777215))
        self.left_container.setFocusPolicy(Qt.ClickFocus)
        self.left_container.setStyleSheet(u"")
        self.left_container.setFrameShape(QFrame.StyledPanel)
        self.left_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.left_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.img_home = QLabel(self.left_container)
        self.img_home.setObjectName(u"img_home")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.img_home.sizePolicy().hasHeightForWidth())
        self.img_home.setSizePolicy(sizePolicy1)
        self.img_home.setStyleSheet(u"image: url(:/img/enviroment/vision-baja.png);")
        self.img_home.setScaledContents(True)
        self.img_home.setWordWrap(False)
        self.img_home.setTextInteractionFlags(Qt.NoTextInteraction)

        self.verticalLayout.addWidget(self.img_home)

        self.frame_3 = QFrame(self.left_container)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy1.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy1)
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, -1, 0, 0)
        self.info_label = QLabel(self.frame_3)
        self.info_label.setObjectName(u"info_label")
        self.info_label.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.info_label.setWordWrap(True)
        self.info_label.setTextInteractionFlags(Qt.LinksAccessibleByMouse|Qt.TextSelectableByMouse)

        self.verticalLayout_2.addWidget(self.info_label)

        self.linePasword = QLineEdit(self.frame_3)
        self.linePasword.setObjectName(u"linePasword")
        font = QFont()
        font.setBold(False)
        self.linePasword.setFont(font)
        self.linePasword.setMaxLength(50)
        self.linePasword.setClearButtonEnabled(True)

        self.verticalLayout_2.addWidget(self.linePasword)


        self.verticalLayout.addWidget(self.frame_3)

        self.button_login = QPushButton(self.left_container)
        self.button_login.setObjectName(u"button_login")
        self.button_login.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.button_login)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.left_container)

        self.right_container = QFrame(Form)
        self.right_container.setObjectName(u"right_container")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(2)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.right_container.sizePolicy().hasHeightForWidth())
        self.right_container.setSizePolicy(sizePolicy2)
        self.right_container.setFrameShape(QFrame.StyledPanel)
        self.right_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.right_container)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_2 = QPushButton(self.right_container)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.scrollArea = QScrollArea(self.right_container)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(2)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy3)
        self.scrollArea.setLayoutDirection(Qt.LeftToRight)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 495, 512))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)


        self.horizontalLayout.addWidget(self.right_container)


        self.retranslateUi(Form)

        self.button_login.setDefault(True)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.img_home.setText("")
        self.info_label.setText(QCoreApplication.translate("Form", u"introduce la palabra magica <3", None))
        self.linePasword.setPlaceholderText(QCoreApplication.translate("Form", u":", None))
        self.button_login.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"agregar", None))
    # retranslateUi

