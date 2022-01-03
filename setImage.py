# 发送图片
import os

import win32con
from ctypes import *
import win32clipboard as w
from PIL import Image

def setImage(imgpath):
    im = Image.open(imgpath)
    im.save('1.bmp')
    aString = windll.user32.LoadImageW(0, r"1.bmp", win32con.IMAGE_BITMAP, 0, 0, win32con.LR_LOADFROMFILE)

    if aString != 0:  ## 由于图片编码问题  图片载入失败的话  aString 就等于0
        w.OpenClipboard()
        w.EmptyClipboard()
        w.SetClipboardData(win32con.CF_BITMAP, aString)
        w.CloseClipboard()
# 获取无后缀的图片名称
def getNosuffixImgName(imgname):
    return os.path.splitext(imgname)[0]