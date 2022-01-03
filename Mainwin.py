# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Mainwin.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!
import os
import sys
import time
import pandas as pd

from Search import searchByUser
from SendInfo import sendInfo
from setImage import setImage
from setText import setText
from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import *



class Ui_Wechat_Assistant(object):
    def setupUi(self, Wechat_Assistant):
        Wechat_Assistant.setObjectName("Wechat_Assistant")
        Wechat_Assistant.resize(1033, 800)
        Wechat_Assistant.setMaximumSize(QtCore.QSize(1033, 800))
        Wechat_Assistant.setStyleSheet("background-color: rgb(20, 211, 106);\n""")
        Wechat_Assistant.setIconSize(QtCore.QSize(100, 100))
        self.centralwidget = QtWidgets.QWidget(Wechat_Assistant)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, -1, 1031, 651))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.verticalLayout.setContentsMargins(3, 2, 3, 2)
        self.verticalLayout.setSpacing(8)
        self.verticalLayout.setObjectName("verticalLayout")

        self.LButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.LButton_2.setGeometry(QtCore.QRect(720, 270, 81, 31))
        self.LButton_2.setStyleSheet("color: rgb(170, 0, 127);")
        self.LButton_2.setObjectName("LButton_2")
        self.LButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.LButton_1.setGeometry(QtCore.QRect(720, 150, 81, 31))
        self.LButton_1.setStyleSheet("color: rgb(170, 0, 127);")
        self.LButton_1.setObjectName("LButton_1")
        self.LButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.LButton_3.setGeometry(QtCore.QRect(720, 560, 81, 31))
        self.LButton_3.setStyleSheet("color: rgb(170, 0, 127);")
        self.LButton_3.setObjectName("LButton_3")


        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(670, 670, 131, 41))
        self.pushButton_2.setStyleSheet("font: 14pt \"楷体\";\n"
                                        "color: rgb(170, 0, 127);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(234, 670, 131, 41))
        self.pushButton_1.setStyleSheet("font: 14pt \"楷体\";\n"
                                        "color: rgb(170, 0, 127);")
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(446, 670, 131, 41))
        self.pushButton_3.setStyleSheet("font: 14pt \"楷体\";\n"
                                        "color: rgb(170, 0, 127);")



        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(390, 270, 321, 31))
        self.textEdit_2.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);\n"
"font: 11pt \"楷体\";")
        self.textEdit_2.setReadOnly(False)
        self.textEdit_2.setObjectName("textEdit_2")

        self.Designer = QtWidgets.QLabel(self.centralwidget)
        self.Designer.setGeometry(QtCore.QRect(780, 750, 231, 41))
        self.Designer.setStyleSheet("font: 9pt \"幼圆\";\n"
"color: rgb(255, 170, 127);\n"
"font: 12pt \"楷体\";")
        self.Designer.setObjectName("Designer")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(230, 270, 141, 41))
        self.label_2.setStyleSheet("font: 9pt \"幼圆\";\n"
"font: 12pt \"楷体\";")
        self.label_2.setObjectName("label_2")

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(230, 150, 141, 41))
        self.label_1.setStyleSheet("font: 9pt \"幼圆\";\n"
"font: 12pt \"楷体\";")
        self.label_1.setObjectName("label_1")


        self.textEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_3.setGeometry(QtCore.QRect(390, 400, 415, 81))
        self.textEdit_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"楷体\";")
        self.textEdit_3.setReadOnly(False)
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_4.setGeometry(QtCore.QRect(390, 560, 321, 51))
        self.textEdit_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                      "font: 11pt \"楷体\";")
        self.textEdit_4.setReadOnly(False)
        self.textEdit_4.setObjectName("textEdit_4")


        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 400, 141, 41))
        self.label_3.setStyleSheet("font: 9pt \"幼圆\";\n"
"font: 12pt \"楷体\";")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(230, 550, 141, 41))
        self.label_5.setStyleSheet("font: 9pt \"幼圆\";\n"
                                   "font: 12pt \"楷体\";")
        self.label_5.setObjectName("label_5")
        self.iteam = QtWidgets.QLabel(self.centralwidget)
        self.iteam.setGeometry(QtCore.QRect(350, 10, 311, 71))
        self.iteam.setStyleSheet("font: 24pt \"楷体\";\n"
"color: rgb(60, 138, 255);\n"
"background-color: rgb(20, 211, 106);")
        self.iteam.setObjectName("iteam")
        self.textEdit_1 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_1.setGeometry(QtCore.QRect(390, 150, 321, 31))
        self.textEdit_1.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 11pt \"楷体\";")
        self.textEdit_1.setReadOnly(False)
        self.textEdit_1.setObjectName("textEdit_1")
        self.label_4= QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 750, 235, 31))
        self.label_4.setStyleSheet("\n"
"font: 11pt \"楷体\"; QtextEdit{border-width:0;border-style:outset}")
        #self.label_4.setReadOnly(True)
        self.label_4.setObjectName("textEdit_4")
        #实时显示时间
        self.timber=QTimer()
        self.timber.timeout.connect(self.showTime)
        self.timber.start(1000)

        Wechat_Assistant.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Wechat_Assistant)
        self.statusbar.setObjectName("statusbar")
        Wechat_Assistant.setStatusBar(self.statusbar)

        self.retranslateUi(Wechat_Assistant)
        QtCore.QMetaObject.connectSlotsByName(Wechat_Assistant)
        '''icon=QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".image\图标2.ico"),QtGui.QIcon.Normal,QtGui.QIcon.off)'''
    def showTime(self):
        datetime=QDateTime.currentDateTime()
        text=datetime.toString('yyyy-MM-dd hh:mm:ss dddd')
        self.label_4.setText(text)


    def retranslateUi(self, Wechat_Assistant):
        _translate = QtCore.QCoreApplication.translate
        Wechat_Assistant.setWindowTitle(_translate("Wechat_Assistant", "Wechat_Assistant"))
        self.LButton_2.setText(_translate("Wechat_Assistant", "选择文件夹"))
        self.LButton_1.setText(_translate("Wechat_Assistant", "选择文件"))

        self.Designer.setText(_translate("Wechat_Assistant", "<html><head/><body><p align=\"center\">Designed by Yuanmei He</p></body></html>"))
        self.label_2.setText(_translate("Wechat_Assistant", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#aa007f;\">请导入图片：</span></p></body></html>"))
        self.pushButton_2.setText(_translate("Wechat_Assistant", "退出"))
        self.pushButton_3.setText(_translate("Wechat_Assistant", "清除"))
        self.label_1.setText(_translate("Wechat_Assistant", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; color:#aa007f;\">请导入名单：</span></p></body></html>"))
        self.LButton_3.setText(_translate("Wechat_Assistant", "从文件中选"))
        self.pushButton_1.setWhatsThis(_translate("Wechat_Assistant", "<html><head/><body><p align=\"center\">s\'d\'f</p></body></html>"))
        self.pushButton_1.setText(_translate("Wechat_Assistant", "确定"))
        self.label_3.setText(_translate("Wechat_Assistant", "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; color:#aa007f;\">消 息 一 ：</span></p></body></html>"))
        self.label_5.setText(_translate("Wechat_Assistant",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:15pt; color:#aa007f;\">消 息 二 ：</span></p></body></html>"))

        self.iteam.setText(_translate("Wechat_Assistant", "<html><head/><body><p><span style=\" color:#aa007f;\">微信群发小助手</span></p></body></html>"))
        Wechat_Assistant.setWindowIcon(QIcon('E:/python数据分析师/Wechat_bot/image/111.ico'))
        self.LButton_1.clicked.connect(self.open_file1)
        self.LButton_2.clicked.connect(self.open_directory)
        self.pushButton_2.clicked.connect(self.clickButtonClose)
        self.LButton_3.clicked.connect(self.open_file2)
        self.pushButton_3.clicked.connect(self.textEdit_3.clear)
        self.pushButton_1.clicked.connect(self.Pushbutton)
    def open_file1(self):
        self.textEdit_1.setText(None)
        caption='打开文件'
        directory='C:/'
        filter='All Files(*.*)'
        initialFilter='All Files(*.*)'
        file_choose,ok=QFileDialog.getOpenFileName(None,caption,directory,filter,initialFilter)#起始路径默认为当前程序所在路径
        print(file_choose)
        self.textEdit_1.setText(file_choose)
        print(ok)
        if file_choose=="":
            print("\n取消选择")
            return
    def open_file2(self):
        self.textEdit_4.setText(None)
        caption='打开文件'
        directory='C:/'
        filter='All Files(*.*)'
        initialFilter='All Files(*.*)'
        file_choose,ok=QFileDialog.getOpenFileName(None,caption,directory,filter,initialFilter)#起始路径默认为当前程序所在路径
        #print(file_choose)
        self.textEdit_4.setText(file_choose)
        #print(ok)
        if file_choose=="":
           # print("\n取消选择")
            return
    def open_directory(self):
        self.textEdit_2.setText(None)
        caption = '打开文件夹'
        directory1= 'C:/'
        dirctory=QFileDialog.getExistingDirectory(None,caption,directory1)

        self.textEdit_2.setText(dirctory)
    def clickButtonClose(self):

        qApp=QApplication.instance()
        qApp.quit()

    def Pushbutton(self):

        info2=self.textEdit_4.toPlainText()
        info1=self.textEdit_3.toPlainText()

        namepath=self.textEdit_1.toPlainText()
        imagepath=self.textEdit_2.toPlainText()


        if namepath is not None:
            if os.path.isfile(namepath):
                #name=namepath.split('/')
                f=open(namepath,'rb')
                xlsx = pd.read_excel(f,sheet_name='Sheet1')
                f.close()
                data = xlsx.names
                print(len(data))
            else:
                data=[]
                data.append(namepath)
        else:
            reply=QMessageBox.warning(None,'警告','请输入/导入微信昵称',
                                            QMessageBox.Ok,QMessageBox.Close)

            return


        if os.path.exists(imagepath):
            imgdir = self.textEdit_2.toPlainText()+'/'
            print(imgdir)
            imgs = os.listdir(imgdir)
            if(len(imgs)):
                for i in range(len(data)):
                    searchByUser(str(data[i]))
                    if(info1 is not None):
                        setText(info1)
                        sendInfo()
                        time.sleep(1)
                    setImage(imgdir + imgs[i])
                    sendInfo()
                    time.sleep(2)
                    if (info2 is not None):
                        if os.path.isfile(info2):
                            f = open(info2, encoding='utf-8')
                            content=f.read()
                            print(content)
                            setText(content)
                            sendInfo()
                            time.sleep(1)
                            f.close()
                        else:
                            setText(info2)
                            sendInfo()
                            time.sleep(1)


            else:
                reply = QMessageBox.information(None, '提示', '该文件夹没有图片！',
                                            QMessageBox.Ok,QMessageBox.Close)
                return


        else:
            reply = QMessageBox.warning(None, "警告", "该文件夹不存在！",
                                            QMessageBox.Ok,QMessageBox.Close)
            return


