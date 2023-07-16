from ui.post_window import *
from PySide6.QtCore import QRect

app = QApplication()
resolution = app.primaryScreen().geometry().getRect()
width,height = [resolution[-2],resolution[-1]]
window = MainWindow()
window.setGeometry(width//4,height//4,width//2,height//2)
window.show()
app.exec()