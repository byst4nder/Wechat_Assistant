import win32con
import win32clipboard as w
# 发送文字
def setText(info):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, info)
    w.CloseClipboard()

