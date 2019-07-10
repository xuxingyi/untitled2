from new1 import Ui_controller
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
import serial


class Cacular(QWidget, Ui_controller):
    """docstring for Cacular"""
    def __init__(self):
        super(Cacular, self).__init__()
        self.setupUi(self)
        self.connecter()
        self.show()

    def connecttomachine(self):
        global ser
        try:
            ser = serial.Serial()
            ser.port = '/dev/ttyUSB0'
            ser.baudrate = 9600
            ser.timeout = 0.2
            ser.open()
            if(ser.read(4) == 'OK/r/n'):
                self.lineEditxxy_imformation.setText('READY!')
            else:
                self.lineEditxxy_imformation.setText('cannot connect!')

        except:
            self.lineEditxxy_imformation.setText('cannot connect!')

    def ps_11(self):
        global ser
        try:
            ser.write('H:1/r/n'.encode())
            ser.readall()
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_21(self):
        global ser
        try:
            ser.write('H:2/r/n'.encode())
            ser.readall()
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_31(self):
        global ser
        try:
            ser.write('H:3/r/n'.encode())
            ser.readall()
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_41(self):
        global ser
        try:
            ser.write('H:4/r/n'.encode())
            ser.readall()
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_11(self):
        global ser
        try:
            ser.write('L:1/r/n'.encode())
            ser.readall()
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_21(self):
        global ser
        try:
            ser.write('L:2/r/n'.encode())
            ser.readall()
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_21(self):
        global ser
        try:
            ser.write('L:2/r/n'.encode())
            ser.readall()
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_31(self):
        global ser
        try:
            ser.write('L:3/r/n'.encode())
            ser.readall()
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_41(self):
        global ser
        try:
            ser.write('L:4/r/n'.encode())
            ser.readall()
        except:
            self.lineEditxxy_imformation.setText('error!')





    def ps_CE(self):
        self.lineEdit.clear()

    def ps_Num_1(self):
        self.lineEdit.insert('1')

    def ps_Num_0(self):
        self.lineEdit.insert('0')

    def ps_Num_2(self):
        self.lineEdit.insert('2')

    def ps_Num_3(self):
        self.lineEdit.insert('3')

    def ps_Num_4(self):
        self.lineEdit.insert('4')

    def ps_Num_5(self):
        self.lineEdit.insert('5')

    def ps_Num_6(self):
        self.lineEdit.insert('6')

    def ps_Num_7(self):
        self.lineEdit.insert('7')

    def ps_Num_8(self):
        self.lineEdit.insert('8')

    def ps_Num_9(self):
        self.lineEdit.insert('9')

    def ps_plus(self):
        self.lineEdit.insert('+')

    def ps_minus(self):
        self.lineEdit.insert('-')

    def ps_multi(self):
        self.lineEdit.insert('*')

    def ps_devide(self):
        self.lineEdit.insert('/')

    def connecter(self):
        self.Num_0.clicked.connect(self.ps_Num_0)
        self.Num_1.clicked.connect(self.ps_Num_1)
        self.Num_2.clicked.connect(self.ps_Num_2)
        self.Num_3.clicked.connect(self.ps_Num_3)
        self.Num_4.clicked.connect(self.ps_Num_4)
        self.Num_5.clicked.connect(self.ps_Num_5)
        self.Num_6.clicked.connect(self.ps_Num_6)
        self.Num_7.clicked.connect(self.ps_Num_7)
        self.Num_8.clicked.connect(self.ps_Num_8)
        self.Num_9.clicked.connect(self.ps_Num_9)
        self.OP_plus.clicked.connect(self.ps_plus)
        self.OP_minus.clicked.connect(self.ps_minus)
        self.OP_multi.clicked.connect(self.ps_multi)
        self.OP_devide.clicked.connect(self.ps_devide)
        self.OP_equal.clicked.connect(self.calcu)
        self.CE.clicked.connect(self.ps_CE)

    def calcu(self):
        text = self.lineEdit.text()
        try:
            result = eval(text)
            self.lineEdit.setText(str(eval(text)))
        except:
            self.lineEdit.setText('invalid syntax, check your input!')


if __name__ == '__main__':
    global ser
    app = QApplication(sys.argv)
    Ca = Cacular()
    sys.exit(app.exec_())
