# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(768, 360)
        font = QtGui.QFont()
        font.setPointSize(9)
        MainWindow.setFont(font)
        MainWindow.setTabletTracking(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(73, 51, 36, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(350, 40, 21, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(540, 40, 21, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_6.setFont(font)
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(490, 40, 36, 21))
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(31, 51, 36, 16))
        font = QtGui.QFont()
        font.setKerning(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(73, 111, 36, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(31, 111, 36, 16))
        font = QtGui.QFont()
        font.setKerning(False)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(73, 171, 36, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(31, 171, 36, 16))
        font = QtGui.QFont()
        font.setKerning(False)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(73, 231, 36, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(31, 231, 36, 16))
        font = QtGui.QFont()
        font.setKerning(False)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(380, 40, 101, 24))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(178, 110, 40, 24))
        self.pushButton_11.setTabletTracking(False)
        self.pushButton_11.setStyleSheet("")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(224, 110, 40, 24))
        self.pushButton_12.setTabletTracking(False)
        self.pushButton_12.setStyleSheet("")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(131, 110, 41, 24))
        self.pushButton_13.setTabletTracking(False)
        self.pushButton_13.setStyleSheet("")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(270, 110, 40, 24))
        self.pushButton_14.setTabletTracking(False)
        self.pushButton_14.setStyleSheet("")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(178, 170, 40, 24))
        self.pushButton_19.setTabletTracking(False)
        self.pushButton_19.setStyleSheet("")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(224, 170, 40, 24))
        self.pushButton_20.setTabletTracking(False)
        self.pushButton_20.setStyleSheet("")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton_21 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_21.setGeometry(QtCore.QRect(131, 170, 41, 24))
        self.pushButton_21.setTabletTracking(False)
        self.pushButton_21.setStyleSheet("")
        self.pushButton_21.setObjectName("pushButton_21")
        self.pushButton_22 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_22.setGeometry(QtCore.QRect(270, 170, 40, 24))
        self.pushButton_22.setTabletTracking(False)
        self.pushButton_22.setStyleSheet("")
        self.pushButton_22.setObjectName("pushButton_22")
        self.pushButton_23 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_23.setGeometry(QtCore.QRect(178, 230, 40, 24))
        self.pushButton_23.setTabletTracking(False)
        self.pushButton_23.setStyleSheet("")
        self.pushButton_23.setObjectName("pushButton_23")
        self.pushButton_24 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_24.setGeometry(QtCore.QRect(224, 230, 40, 24))
        self.pushButton_24.setTabletTracking(False)
        self.pushButton_24.setStyleSheet("")
        self.pushButton_24.setObjectName("pushButton_24")
        self.pushButton_25 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_25.setGeometry(QtCore.QRect(131, 230, 41, 24))
        self.pushButton_25.setTabletTracking(False)
        self.pushButton_25.setStyleSheet("")
        self.pushButton_25.setObjectName("pushButton_25")
        self.pushButton_26 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_26.setGeometry(QtCore.QRect(270, 230, 40, 24))
        self.pushButton_26.setTabletTracking(False)
        self.pushButton_26.setStyleSheet("")
        self.pushButton_26.setObjectName("pushButton_26")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(490, 110, 36, 21))
        self.label_10.setObjectName("label_10")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(380, 110, 101, 24))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_27 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_27.setGeometry(QtCore.QRect(540, 110, 21, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_27.setFont(font)
        self.pushButton_27.setObjectName("pushButton_27")
        self.pushButton_28 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_28.setGeometry(QtCore.QRect(350, 110, 21, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_28.setFont(font)
        self.pushButton_28.setObjectName("pushButton_28")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(490, 170, 36, 21))
        self.label_11.setObjectName("label_11")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(380, 170, 101, 24))
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton_29 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_29.setGeometry(QtCore.QRect(540, 170, 21, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_29.setFont(font)
        self.pushButton_29.setObjectName("pushButton_29")
        self.pushButton_30 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_30.setGeometry(QtCore.QRect(350, 170, 21, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_30.setFont(font)
        self.pushButton_30.setObjectName("pushButton_30")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(490, 230, 36, 21))
        self.label_12.setObjectName("label_12")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(380, 230, 101, 24))
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_31 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_31.setGeometry(QtCore.QRect(540, 230, 21, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_31.setFont(font)
        self.pushButton_31.setObjectName("pushButton_31")
        self.pushButton_32 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_32.setGeometry(QtCore.QRect(350, 230, 21, 29))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_32.setFont(font)
        self.pushButton_32.setObjectName("pushButton_32")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(590, 40, 171, 221))
        self.graphicsView.setObjectName("graphicsView")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(30, 270, 80, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(131, 48, 41, 24))
        self.pushButton_7.setTabletTracking(False)
        self.pushButton_7.setStyleSheet("")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(178, 48, 40, 24))
        self.pushButton_8.setTabletTracking(False)
        self.pushButton_8.setStyleSheet("")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(270, 48, 40, 24))
        self.pushButton_10.setTabletTracking(False)
        self.pushButton_10.setStyleSheet("")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(224, 48, 40, 24))
        self.pushButton_9.setTabletTracking(False)
        self.pushButton_9.setStyleSheet("")
        self.pushButton_9.setObjectName("pushButton_9")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 768, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        MainWindow.setToolTip(_translate("MainWindow", "<html><head/><body><p>0.0</p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "degree"))
        self.pushButton_5.setToolTip(_translate("MainWindow", "<html><head/><body><p>smaller</p></body></html>"))
        self.pushButton_5.setText(_translate("MainWindow", "<"))
        self.pushButton_6.setToolTip(_translate("MainWindow", "<html><head/><body><p>bigger</p></body></html>"))
        self.pushButton_6.setText(_translate("MainWindow", ">"))
        self.label_3.setText(_translate("MainWindow", "degree"))
        self.label.setToolTip(_translate("MainWindow", "<html><head/><body><p>current position</p></body></html>"))
        self.label.setText(_translate("MainWindow", "0"))
        self.label_4.setText(_translate("MainWindow", "degree"))
        self.label_5.setToolTip(_translate("MainWindow", "<html><head/><body><p>current position</p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "0"))
        self.label_6.setText(_translate("MainWindow", "mm"))
        self.label_7.setToolTip(_translate("MainWindow", "<html><head/><body><p>current position</p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "0"))
        self.label_8.setText(_translate("MainWindow", "mm"))
        self.label_9.setToolTip(_translate("MainWindow", "<html><head/><body><p>current position</p></body></html>"))
        self.label_9.setText(_translate("MainWindow", "0"))
        self.lineEdit.setToolTip(_translate("MainWindow", "<html><head/><body><p>how much will move</p></body></html>"))
        self.pushButton_11.setToolTip(_translate("MainWindow", "<html><head/><body><p>stop move</p></body></html>"))
        self.pushButton_11.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>stop move</p></body></html>"))
        self.pushButton_11.setText(_translate("MainWindow", "stop"))
        self.pushButton_12.setToolTip(_translate("MainWindow", "<html><head/><body><p>Move to the 0 position</p></body></html>"))
        self.pushButton_12.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>stop move</p></body></html>"))
        self.pushButton_12.setText(_translate("MainWindow", "to 0"))
        self.pushButton_13.setToolTip(_translate("MainWindow", "<html><head/><body><p>Move to the machine origin</p></body></html>"))
        self.pushButton_13.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>stop move</p></body></html>"))
        self.pushButton_13.setText(_translate("MainWindow", "home"))
        self.pushButton_14.setToolTip(_translate("MainWindow", "<html><head/><body><p>Set the current position to zero</p></body></html>"))
        self.pushButton_14.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>stop move</p></body></html>"))
        self.pushButton_14.setText(_translate("MainWindow", "0 set"))
        self.pushButton_19.setToolTip(_translate("MainWindow", "<html><head/><body><p>stoop move</p></body></html>"))
        self.pushButton_19.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>stop move</p></body></html>"))
        self.pushButton_19.setText(_translate("MainWindow", "stop"))
        self.pushButton_20.setToolTip(_translate("MainWindow", "<html><head/><body><p>Move to the 0 position</p></body></html>"))
        self.pushButton_20.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>stop move</p></body></html>"))
        self.pushButton_20.setText(_translate("MainWindow", "to 0"))
        self.pushButton_21.setToolTip(_translate("MainWindow", "<html><head/><body><p>Move to the machine origin</p></body></html>"))
        self.pushButton_21.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>stop move</p></body></html>"))
        self.pushButton_21.setText(_translate("MainWindow", "home"))
        self.pushButton_22.setToolTip(_translate("MainWindow", "<html><head/><body><p>Set the current position to zero</p></body></html>"))
        self.pushButton_22.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>stop move</p></body></html>"))
        self.pushButton_22.setText(_translate("MainWindow", "0 set"))
        self.pushButton_23.setToolTip(_translate("MainWindow", "<html><head/><body><p>stop move</p></body></html>"))
        self.pushButton_23.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>stop move</p></body></html>"))
        self.pushButton_23.setText(_translate("MainWindow", "stop"))
        self.pushButton_24.setToolTip(_translate("MainWindow", "<html><head/><body><p>Move to the 0 position</p></body></html>"))
        self.pushButton_24.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>stop move</p></body></html>"))
        self.pushButton_24.setText(_translate("MainWindow", "to 0"))
        self.pushButton_25.setToolTip(_translate("MainWindow", "<html><head/><body><p>Move to the machine origin</p></body></html>"))
        self.pushButton_25.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>stop move</p></body></html>"))
        self.pushButton_25.setText(_translate("MainWindow", "home"))
        self.pushButton_26.setToolTip(_translate("MainWindow", "<html><head/><body><p>Set the current position to zero</p></body></html>"))
        self.pushButton_26.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>stop move</p></body></html>"))
        self.pushButton_26.setText(_translate("MainWindow", "0 set"))
        self.label_10.setText(_translate("MainWindow", "degree"))
        self.lineEdit_2.setToolTip(_translate("MainWindow", "<html><head/><body><p>how much will move</p></body></html>"))
        self.pushButton_27.setToolTip(_translate("MainWindow", "<html><head/><body><p>bigger</p></body></html>"))
        self.pushButton_27.setText(_translate("MainWindow", ">"))
        self.pushButton_28.setToolTip(_translate("MainWindow", "<html><head/><body><p>smaller</p></body></html>"))
        self.pushButton_28.setText(_translate("MainWindow", "<"))
        self.label_11.setText(_translate("MainWindow", "mm"))
        self.lineEdit_3.setToolTip(_translate("MainWindow", "<html><head/><body><p>how much will move</p></body></html>"))
        self.pushButton_29.setToolTip(_translate("MainWindow", "<html><head/><body><p>bigger</p></body></html>"))
        self.pushButton_29.setText(_translate("MainWindow", ">"))
        self.pushButton_30.setToolTip(_translate("MainWindow", "<html><head/><body><p>smaller</p></body></html>"))
        self.pushButton_30.setText(_translate("MainWindow", "<"))
        self.label_12.setText(_translate("MainWindow", "mm"))
        self.lineEdit_4.setToolTip(_translate("MainWindow", "<html><head/><body><p>how much will move</p></body></html>"))
        self.pushButton_31.setToolTip(_translate("MainWindow", "<html><head/><body><p>bigger</p></body></html>"))
        self.pushButton_31.setText(_translate("MainWindow", ">"))
        self.pushButton_32.setToolTip(_translate("MainWindow", "<html><head/><body><p>smaller</p></body></html>"))
        self.pushButton_32.setText(_translate("MainWindow", "<"))
        self.graphicsView.setToolTip(_translate("MainWindow", "<html><head/><body><p>the synchro optical image</p></body></html>"))
        self.pushButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>refresh all data</p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "refresh"))
        self.pushButton_7.setToolTip(_translate("MainWindow", "<html><head/><body><p>Move to the machine origin</p></body></html>"))
        self.pushButton_7.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>stop move</p></body></html>"))
        self.pushButton_7.setText(_translate("MainWindow", "home"))
        self.pushButton_8.setToolTip(_translate("MainWindow", "<html><head/><body><p>stop move</p></body></html>"))
        self.pushButton_8.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>stop move</p></body></html>"))
        self.pushButton_8.setText(_translate("MainWindow", "stop"))
        self.pushButton_10.setToolTip(_translate("MainWindow", "<html><head/><body><p>Set the current position to zero</p></body></html>"))
        self.pushButton_10.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>stop move</p></body></html>"))
        self.pushButton_10.setText(_translate("MainWindow", "0 set"))
        self.pushButton_9.setToolTip(_translate("MainWindow", "<html><head/><body><p>Move to the 0 position</p></body></html>"))
        self.pushButton_9.setWhatsThis(_translate("MainWindow", "<html><head/><body><p>stop move</p></body></html>"))
        self.pushButton_9.setText(_translate("MainWindow", "to 0"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())