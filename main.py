from ui.post_window import *

if __name__ == '__main__':
    app = QApplication()
    resolution = app.primaryScreen().geometry().getRect()
    width,height = [resolution[-2],resolution[-1]]
    window = MainWindow()
    window.setGeometry(width//4,height//4,width//2,height//2)
    window.show()
    app.exec()
