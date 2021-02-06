import cv2, pyautogui, keyboard, time, win32gui, win32con, win10toast
import numpy as np
from win32api import GetSystemMetrics
"""
Copyright 2021. codingPro01. All Rights Reserved.
Credits: https://www.thepythoncode.com/article/make-screen-recorder-python, https://www.thepythoncode.com/code/make-screen-recorder-python
"""
SCREEN_SIZE = (GetSystemMetrics(0), GetSystemMetrics(1))
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))
a = True
Minimize = win32gui.GetForegroundWindow()
win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)
toast = win10toast.ToastNotifier()
toast.show_toast("Screen record notification", "Your recording started.", duration=2)
time.sleep(2.5)
while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    """
    cv2.imshow("screenshot", frame)
    while a:
        Minimize = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)
        a = False
    """
    if keyboard.is_pressed("right_ctrl") == True and keyboard.is_pressed("left_ctrl") == True:
        break
toast.show_toast("Screen record notification", "Your recording ended.", duration=3)
cv2.destroyAllWindows()
out.release()
