import sys
from PyQt5.QtWidgets import QApplication,QWidget

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(800,400)
    w.move(200,200)
    w.setWindowTitle('四维移动平台')
    w.show()
    sys.exit(app.exec_())
