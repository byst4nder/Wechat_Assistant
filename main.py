


'''imgdir = 'imgs/'
imgs = os.listdir(imgdir)
for img in imgs:
    searchByUser(getNosuffixImgName(img))
    setImage(imgdir + img)
    sendInfo()
    time.sleep(1)'''
import sys
import time

from PyQt5 import Qt
from qtpy import QtWidgets

from Mainwin import Ui_Wechat_Assistant
from Search import searchByUser, closeByUser
from SendInfo import sendInfo
from setText import setText


'''def main():
    
    searchByUser('Ve')

    setText('like')
    sendInfo()
    time.sleep(1)
    searchByUser('文件传输助手')
    setText('文件')
    sendInfo()

main()'''

if __name__ == '__main__':
    WechatApp = Qt.QApplication(sys.argv)
    WechatApp.processEvents()
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_Wechat_Assistant()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(WechatApp.exec_())