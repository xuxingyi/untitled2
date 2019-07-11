from new1 import Ui_controller
import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
import serial


class Cacular(QMainWindow, Ui_controller):
    """docstring for Cacular"""
    def __init__(self):
        super(Cacular, self).__init__()
        self.setupUi(self)
        self.connecter()
        self.show()

    def ps_connect(self):
        global ser
        try:
            ser = serial.Serial()
            ser.port = '/dev/ttyUSB0'
            ser.baudrate = 9600
            ser.timeout = 0.2
            ser.open()
            if(ser.read(4) == 'OK\r\n'):
                self.lineEditxxy_imformation.setText('READY!')
            else:
                self.lineEditxxy_imformation.setText('smenthing wrong about the machine!')

        except:
            self.lineEditxxy_imformation.setText('cannot connect,maybe the COM has been occupied!')

    def ps_disconcect(self):
        global ser
        try:
            ser.close()
        except:
            self.lineEditxxy_imformation.setText('you have not connect before!')



    def ps_11(self):
        global ser
        try:
            ser.write('H:1\r\n'.encode())
            ser.readall()
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_21(self):
        global ser
        try:
            ser.write('H:2\r\n'.encode())
            ser.readall()
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_31(self):
        global ser
        try:
            ser.write('H:3\r\n'.encode())
            ser.readall()
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_41(self):
        global ser
        try:
            ser.write('H:4\r\n'.encode())
            ser.readall()
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_12(self):
        global ser
        try:
            ser.write('L:1\r\n'.encode())
            ser.readall()
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_22(self):
        global ser
        try:
            ser.write('L:2\r\n'.encode())
            ser.readall()
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_32(self):
        global ser
        try:
            ser.write('L:3\r\n'.encode())
            ser.readall()
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_42(self):
        global ser
        try:
            ser.write('L:4\r\n'.encode())
            ser.readall()
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_13(self):
        global ser
        try:
            ser.write('A:1+P0\r\n'.encode())
            ser.readall()
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_23(self):
        global ser
        try:
            ser.write('A:2+P0\r\n'.encode())
            ser.readall()
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_33(self):
        global ser
        try:
            ser.write('A:3+P0\r\n'.encode())
            ser.readall()
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_43(self):
        global ser
        try:
            ser.write('A:4+P0\r\n'.encode())
            ser.readall()
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_14(self):
        global ser
        try:
            ser.write('R:1\r\n'.encode())
            ser.readall()
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_24(self):
        global ser
        try:
            ser.write('R:2\r\n'.encode())
            ser.readall()
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_34(self):
        global ser
        try:
            ser.write('R:3\r\n'.encode())
            ser.readall()
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_44(self):
        global ser
        try:
            ser.write('R:4\r\n'.encode())
            ser.readall()
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_19(self):
        global ser
        str12='M:1-P'+self.lineEditxxy_12.text()+'\r\n'
        try:
            ser.write(str12.encode())
            ser.readall()
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_25(self):
        global ser
        str22='M:2-P'+self.lineEditxxy_22.text()+'\r\n'
        try:
            ser.write(str22.encode())
            ser.readall()
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_35(self):
        global ser
        str32='M:3-P'+self.lineEditxxy_32.text()+'\r\n'
        try:
            ser.write(str32.encode())
            ser.readall()
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_45(self):
        global ser
        str42='M:4-P'+self.lineEditxxy_42.text()+'\r\n'
        try:
            ser.write(str42.encode())
            ser.readall()
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_20(self):
        global ser
        str13='M:1+P'+self.lineEditxxy_12.text()+'\r\n'
        try:
            ser.write(str13.encode())
            ser.readall()
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_26(self):
        global ser
        str23='M:2+P'+self.lineEditxxy_22.text()+'\r\n'
        try:
            ser.write(str23.encode())
            ser.readall()
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_36(self):
        global ser
        str33='M:3+P'+self.lineEditxxy_32.text()+'\r\n'
        try:
            ser.write(str33.encode())
            ser.readall()
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_46(self):
        global ser
        str43='M:4+P'+self.lineEditxxy_42.text()+'\r\n'
        try:
            ser.write(str43.encode())
            ser.readall()
        except:
            self.lineEditxxy_imformation.setText('error!')


    def connecter(self):
        self.pushButton_concect.clicked.connect(self.ps_connect)
        self.pushButton_disconnect.clicked.connect(self.ps_disconcect)
        self.pushButton_11.clicked.connect(self.ps_11)
        self.pushButton_21.clicked.connect(self.ps_21)
        self.pushButton_31.clicked.connect(self.ps_31)
        self.pushButton_41.clicked.connect(self.ps_41)
        self.pushButton_12.clicked.connect(self.ps_12)
        self.pushButton_22.clicked.connect(self.ps_22)
        self.pushButton_32.clicked.connect(self.ps_32)
        self.pushButton_42.clicked.connect(self.ps_42)
        self.pushButton_13.clicked.connect(self.ps_13)
        self.pushButton_23.clicked.connect(self.ps_23)
        self.pushButton_33.clicked.connect(self.ps_33)
        self.pushButton_43.clicked.connect(self.ps_43)
        self.pushButton_41.clicked.connect(self.ps_41)
        self.pushButton_42.clicked.connect(self.ps_42)
        self.pushButton_43.clicked.connect(self.ps_43)
        self.pushButton_44.clicked.connect(self.ps_44)
        self.pushButton_11.clicked.connect(self.ps_11)
        self.pushButton_11.clicked.connect(self.ps_11)




        # self.CE.clicked.connect(self.ps_CE)

    # def calcu(self):
    #     text = self.lineEdit.text()
    #     try:
    #         result = eval(text)
    #         self.lineEdit.setText(str(eval(text)))
    #     except:
    #         self.lineEdit.setText('invalid syntax, check your input!')


if __name__ == '__main__':
    global ser
    app = QApplication(sys.argv)
    Ca = Cacular()
    sys.exit(app.exec_())
