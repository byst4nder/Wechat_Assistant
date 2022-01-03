
import time
import win32api
import win32con
import win32gui
from Click_Paste import m_click, pasteInfo, CopyInfo
from setText import setText

# 定位微信窗口，进行昵称备注的搜索（需点击两下才能获取到焦点）
def searchByUser(uname):
    hwnd = win32gui.FindWindow('WeChatMainWndForPC', '微信')
    setText(uname)
    #CopyInfo()
    print(uname)
    m_click(128, 40)
    time.sleep(0.5)
    m_click(128, 40)
    pasteInfo()
    time.sleep(3)
    m_click(120, 120)  # 搜索到之后点击
    # win32api.keybd_event(13,0,0,0)#回车
    # win32api.keybd_event(13,0,KEYEVENTF_KEYUP,0)
    # win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    # win32gui.SendMessage(hwnd, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

# 发送完信息之后关闭窗口(跟QQ不一样，可以不关闭），接着搜索发送
def closeByUser(uname):
    hwnd = win32gui.FindWindow('WeChatMainWndForPC', '微信')
    win32api.keybd_event(18, 0, 0, 0)  # Alt
    win32api.keybd_event(115, 0, 0, 0)  # F4
    win32api.keybd_event(115, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(18, 0, win32con.KEYEVENTF_KEYUP, 0)
