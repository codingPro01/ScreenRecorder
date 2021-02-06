import cv2, pyautogui, keyboard, time, win32gui, win32con
import numpy as np
from win32api import GetSystemMetrics

SCREEN_SIZE = (GetSystemMetrics(0), GetSystemMetrics(1))
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (SCREEN_SIZE))
a = True
while True:
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow("screenshot", frame)
    while a:
        Minimize = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(Minimize, win32con.SW_MINIMIZE)
        a = False
    if keyboard.is_pressed("right_ctrl") == True and keyboard.is_pressed("left_ctrl") == True:
        break

cv2.destroyAllWindows()
out.release()