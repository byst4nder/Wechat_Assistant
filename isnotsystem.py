
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QFileInfo
from PyQt5.QtWidgets import QFileDialog


class Ui_Form(object):
    save_path = ''

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(484, 412)
        self.open_path_text = QtWidgets.QLineEdit(Form)
        self.open_path_text.setGeometry(QtCore.QRect(40, 20, 331, 20))
        self.open_path_text.setObjectName("open_path_text")
        self.open_path_but = QtWidgets.QPushButton(Form)
        self.open_path_but.setGeometry(QtCore.QRect(380, 20, 75, 23))
        self.open_path_but.setObjectName("open_path_but")
        self.save_path_but = QtWidgets.QPushButton(Form)
        self.save_path_but.setGeometry(QtCore.QRect(380, 50, 75, 23))
        self.save_path_but.setObjectName("save_path_but")
        self.save_path_text = QtWidgets.QLineEdit(Form)
        self.save_path_text.setGeometry(QtCore.QRect(40, 50, 331, 20))
        self.save_path_text.setObjectName("save_path_text")
        self.text_value = QtWidgets.QTextEdit(Form)
        self.text_value.setGeometry(QtCore.QRect(10, 90, 461, 281))
        self.text_value.setObjectName("text_value")
        self.save_but = QtWidgets.QPushButton(Form)
        self.save_but.setGeometry(QtCore.QRect(190, 380, 75, 23))
        self.save_but.setObjectName("save_but")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.open_path_text.setPlaceholderText(_translate("Form", "打开地址"))
        self.open_path_but.setText(_translate("Form", "浏览"))
        self.save_path_but.setText(_translate("Form", "浏览"))
        self.save_path_text.setPlaceholderText(_translate("Form", "保存地址"))
        self.save_but.setText(_translate("Form", "保存"))
        self.open_path_but.clicked.connect(self.open_event)
        self.save_path_but.clicked.connect(self.save_event)
        self.save_but.clicked.connect(self.save_text)

    def open_event(self):
        _translate = QtCore.QCoreApplication.translate
        directory1 = QFileDialog.getOpenFileName(None, "选择文件", "C:/")
        print(directory1)  # 打印文件夹路径
        path = directory1[0]
        self.open_path_text.setText(_translate("Form", path))
        if path is not None:
            with open(file=path, mode='r+', encoding='utf-8') as file:
                self.text_value.setPlainText(file.read())

    def save_event(self):
        global save_path
        _translate = QtCore.QCoreApplication.translate
        fileName2, ok2 = QFileDialog.getSaveFileName(None, "文件保存", "C:/")
        #print(fileName2)  # 打印保存文件的全部路径（包括文件名和后缀名）
        save_path = fileName2
        self.save_path_text.setText(_translate("Form", save_path))

    def save_text(self):
        global save_path
        if save_path is not None:
            with open(file=save_path, mode='a+', encoding='utf-8') as file:
                file.write(self.text_value.toPlainText())
            #print('已保存！')
            self.text_value.clear()

            '''
            directory1 = QFileDialog.getExistingDirectory(self, "选择文件夹", "/")
            print(directory1)  # 打印文件夹路径
            text.setText(_translate("Form", directory1))
            fileName, filetype = QFileDialog.getOpenFileName(self, "选择文件", "/", "All Files (*);;Text Files (*.txt)")
            print(fileName, filetype)  # 打印文件全部路径（包括文件名和后缀名）和文件类型
            print(fileName)  # 打印文件全部路径（包括文件名和后缀名）
            text.setText(_translate("Form", fileName))
            fileinfo = QFileInfo(fileName)
            print(fileinfo)  # 打印与系统相关的文件信息，包括文件的名字和在文件系统中位置，文件的访问权限，是否是目录或符合链接，等等。
            file_name = fileinfo.fileName()
            print(file_name)  # 打印文件名和后缀名
            file_suffix = fileinfo.suffix()
            print(file_suffix)  # 打印文件后缀名
            file_path = fileinfo.absolutePath()
            print(file_path)  # 打印文件绝对路径（不包括文件名和后缀名）
            files, ok1 = QFileDialog.getOpenFileNames(self, "多文件选择", "/", "所有文件 (*);;文本文件 (*.txt)")
            print(files, ok1)  # 打印所选文件全部路径（包括文件名和后缀名）和文件类型
            fileName2, ok2 = QFileDialog.getSaveFileName(self, "文件保存", "/", "图片文件 (*.png);;(*.jpeg)")
            print(fileName2)  # 打印保存文件的全部路径（包括文件名和后缀名）
            '''

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())

