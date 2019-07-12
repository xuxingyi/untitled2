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
            ser.port = 'COM4'
            # ser.port = '/dev/ttyUSB0'
            ser.baudrate = 9600
            ser.timeout = 0.2
            ser.open()
            self.lineEditxxy_imformation.setText('READY!')
            ser.write(''.encode())
        except:
            self.lineEditxxy_imformation.setText('cannot connect,maybe the COM has been occupied!')

    def ps_disconcect(self):
        global ser
        try:
            ser.close()
            self.lineEditxxy_imformation.setText('disconnect!')
        except:
            self.lineEditxxy_imformation.setText('you have not connect before!')



    def ps_11(self):
        global ser
        try:
            ser.write('H:1\r\n'.encode())
            ser.readall()
            self.lineEditxxy_imformation.setText('home1 ok!')
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_21(self):
        global ser
        try:
            ser.write('H:2\r\n'.encode())
            ser.readall()
            self.lineEditxxy_imformation.setText('home2 ok!')
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_31(self):
        global ser
        try:
            ser.write('H:3\r\n'.encode())
            ser.readall()
            self.lineEditxxy_imformation.setText('home3 ok!')
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_41(self):
        global ser
        try:
            ser.write('H:4\r\n'.encode())
            ser.readall()
            self.lineEditxxy_imformation.setText('home4 ok!')
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_12(self):
        global ser
        try:
            ser.write('L:1\r\n'.encode())
            ser.readall()
            self.lineEditxxy_imformation.setText('stop!')
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_22(self):
        global ser
        try:
            ser.write('L:2\r\n'.encode())
            ser.readall()
            self.lineEditxxy_imformation.setText('stop!')
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_32(self):
        global ser
        try:
            ser.write('L:3\r\n'.encode())
            ser.readall()
            self.lineEditxxy_imformation.setText('stop!')
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_42(self):
        global ser
        try:
            ser.write('L:4\r\n'.encode())
            ser.readall()
            self.lineEditxxy_imformation.setText('stop!')
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_13(self):
        global ser
        try:
            ser.write('A:1+P0\r\n'.encode())
            ser.write('G:\r\n'.encode())
            ser.readall()
            self.lineEditxxy_imformation.setText('have moved to 0(electr)!')
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_23(self):
        global ser
        try:
            ser.write('A:2+P0\r\n'.encode())
            ser.write('G:\r\n'.encode())
            ser.readall()
            self.lineEditxxy_imformation.setText('have moved to 0(electr)!')
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_33(self):
        global ser
        try:
            ser.write('A:3+P0\r\n'.encode())
            ser.write('G:\r\n'.encode())
            ser.readall()
            self.lineEditxxy_imformation.setText('have moved to 0(electr)!')
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_43(self):
        global ser
        try:
            ser.write('A:4+P0\r\n'.encode())
            ser.write('G:\r\n'.encode())
            ser.readall()
            self.lineEditxxy_imformation.setText('have moved to 0(electr)!')
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_14(self):
        global ser
        try:
            ser.write('R:1\r\n'.encode())
            ser.readall()
            self.lineEditxxy_imformation.setText('have set to 0(electr)!')
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_24(self):
        global ser
        try:
            ser.write('R:2\r\n'.encode())
            ser.readall()
            self.lineEditxxy_imformation.setText('have set to 0(electr)!')
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_34(self):
        global ser
        try:
            ser.write('R:3\r\n'.encode())
            ser.readall()
            self.lineEditxxy_imformation.setText('have set to 0(electr)!')
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_44(self):
        global ser
        try:
            ser.write('R:4\r\n'.encode())
            ser.readall()
            self.lineEditxxy_imformation.setText('have set to 0(electr)!')
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_19(self):
        global ser
        str12='M:1-P'+self.lineEditxxy_12.text()+'\r\n'
        try:
            ser.write(str12.encode())
            ser.write('G:\r\n'.encode())
            ser.readall()
            self.lineEditxxy_imformation.setText('OK!')
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_25(self):
        global ser
        str22='M:2-P'+self.lineEditxxy_22.text()+'\r\n'
        try:
            ser.write(str22.encode())
            ser.write('G:\r\n'.encode())
            ser.readall()
            self.lineEditxxy_imformation.setText('OK!')
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_35(self):
        global ser
        str32='M:3-P'+self.lineEditxxy_32.text()+'\r\n'
        try:
            ser.write(str32.encode())
            ser.write('G:\r\n'.encode())
            ser.readall()
            self.lineEditxxy_imformation.setText('OK!')
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_45(self):
        global ser
        str42='M:4-P'+self.lineEditxxy_42.text()+'\r\n'

        try:
            ser.write(str42.encode())
            ser.write('G:\r\n'.encode())
            ser.readall()
            self.lineEditxxy_imformation.setText('OK!')
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_20(self):
        global ser
        str13='M:1+P'+self.lineEditxxy_12.text()+'\r\n'

        try:
            ser.write(str13.encode())
            ser.write('G:\r\n'.encode())
            ser.readall()
            self.lineEditxxy_imformation.setText('OK!')
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_26(self):
        global ser
        str23='M:2+P'+self.lineEditxxy_22.text()+'\r\n'
        try:
            ser.write(str23.encode())
            ser.write('G:\r\n'.encode())
            ser.readall()
            self.lineEditxxy_imformation.setText('OK!')
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_36(self):
        global ser
        str33='M:3+P'+self.lineEditxxy_32.text()+'\r\n'
        try:
            ser.write(str33.encode())
            ser.write('G:\r\n'.encode())
            ser.readall()
            self.lineEditxxy_imformation.setText('OK!')
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_46(self):
        global ser
        str43='M:4+P'+self.lineEditxxy_42.text()+'\r\n'
        try:
            ser.write(str43.encode())
            ser.write('G:\r\n'.encode())
            ser.readall()
            self.lineEditxxy_imformation.setText('OK!')
        except:
            self.lineEditxxy_imformation.setText('error!')

    def ps_refresh(self):
        global ser
        try:
            ser.readall()
            ser.write('Q:\r\n'.encode())
            newdata = ser.readall()
            strnewdata = newdata.decode()
            x1 = int(strnewdata[1:10])
            x2 = int(strnewdata[12:21])
            x3 = int(strnewdata[23:32])
            x4 = int(strnewdata[34:43])
            self.lineEditxxy_11.setText(strnewdata[0] + str(x1))
            self.lineEditxxy_21.setText(strnewdata[11] + str(x2))
            self.lineEditxxy_31.setText(strnewdata[22] + str(x3))
            self.lineEditxxy_41.setText(strnewdata[33] + str(x4))
            self.lineEditxxy_imformation.setText('OK!')
        except:
            self.lineEditxxy_imformation.setText('error!')




    def connecter(self):
        self.pushButton_concect.clicked.connect(self.ps_connect)
        self.pushButton_disconnect.clicked.connect(self.ps_disconcect)
        self.pushButton_11.clicked.connect(self.ps_11)
        # self.pushButton_21.clicked.connect(self.ps_21)
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
        self.pushButton_14.clicked.connect(self.ps_14)
        self.pushButton_24.clicked.connect(self.ps_24)
        self.pushButton_34.clicked.connect(self.ps_34)
        self.pushButton_44.clicked.connect(self.ps_44)
        self.pushButton_19.clicked.connect(self.ps_19)
        self.pushButton_20.clicked.connect(self.ps_20)
        self.pushButton_25.clicked.connect(self.ps_25)
        self.pushButton_26.clicked.connect(self.ps_26)
        self.pushButton_35.clicked.connect(self.ps_35)
        self.pushButton_36.clicked.connect(self.ps_36)
        self.pushButton_45.clicked.connect(self.ps_45)
        self.pushButton_46.clicked.connect(self.ps_46)
        self.pushButton_refresh.clicked.connect(self.ps_refresh)







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
