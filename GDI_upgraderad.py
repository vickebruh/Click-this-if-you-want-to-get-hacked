import win32gui
import win32con
import win32api
import random
import time

width = win32api.GetSystemMetrics(0)
height = win32api.GetSystemMetrics(1)
hdc = win32gui.GetDC(0)

try:
    while True:
       
        x = random.randint(0, width - 100)
        y = random.randint(0, height - 100)
        w = random.randint(50, 300)
        h = random.randint(50, 300)
        win32gui.PatBlt(hdc, x, y, w, h, win32con.DSTINVERT)

        
        x1 = random.randint(0, width)
        y1 = random.randint(0, height)
        x2 = random.randint(0, width)
        y2 = random.randint(0, height)
        color = win32api.RGB(random.randint(0, 255),
                             random.randint(0, 255),
                             random.randint(0, 255))
        pen = win32gui.CreatePen(win32con.PS_SOLID, 2, color)
        win32gui.SelectObject(hdc, pen)
        win32gui.MoveToEx(hdc, x1, y1)
        win32gui.LineTo(hdc, x2, y2)
        win32gui.DeleteObject(pen)

        time.sleep(0.01)
except:
    win32gui.ReleaseDC(0, hdc)
