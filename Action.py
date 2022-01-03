import time

from Mainwin import Ui_Wechat_Assistant
import pandas as pd
import os

from Search import searchByUser
from SendInfo import sendInfo
from setImage import setImage
from setText import setText


def Pushbutton():
    info1=Ui_Wechat_Assistant.gettextEdit_3()
    info2=Ui_Wechat_Assistant.gettextEdit_4()
    xlsx = pd.read_excel(Ui_Wechat_Assistant.gettextEdit_1(), sheet_name='原始数据录入')
    data = xlsx.names
    print(len(data))
    imgdir = Ui_Wechat_Assistant.gettextEdit_2()
    imgs = os.listdir(imgdir)
    for i in range(len(data)):
        searchByUser(str(data[i]))
        setText(info2)
        sendInfo()
        time.sleep(1)
        setImage(imgdir + imgs[i])
        sendInfo()
        time.sleep(2)
        setText(info1)
        sendInfo()
        time.sleep(1)