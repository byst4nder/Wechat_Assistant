import time

import win32api
import win32con

from Click_Paste import pasteInfo

def sendInfo():
    time.sleep(1)
    pasteInfo()
    time.sleep(1)
    win32api.keybd_event(18, 0, 0, 0)  # Alt
    win32api.keybd_event(83, 0, 0, 0)  # s
    win32api.keybd_event(83, 0, win32con.KEYEVENTF_KEYUP, 0)  # 释放按键
    win32api.keybd_event(18, 0, win32con.KEYEVENTF_KEYUP, 0)