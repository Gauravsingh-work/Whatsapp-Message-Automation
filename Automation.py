# So Today we will be making automation in python using Pyautogui
import pyautogui
import time
time.sleep(5)
count = 0
while count<=20:
    pyautogui.typewrite("Hii Darling " + str(count))
    pyautogui.press("enter")
    count = count+1