import pyautogui
import cv2
import numpy as np
import time

def clamp(num, min_value, max_value):
   return max(min(num, max_value), min_value)

#print("x1 = ")
#x1 = int(input())
#print("y1 = ")
#y1 = int(input())
#print("x2 = ")
#x2 = int(input())
#print("y2 = ")
#y2 = int(input())
x1 = 1000
y1 = 430
x2 = 450
y2 = 120
im = pyautogui.screenshot(region=(x1, y1, x2, y2))
print(im.getpixel((0, 0)))
while True:
    im = pyautogui.screenshot(region=(x1, y1, x2, y2))
    for i in range(x1, x1 + x2):
        x3 = i - x1
        y3 = clamp((y1+y1+y2)/2, 0, y2 - 1)
        #print()
        #print("se scaneaza ", (x3, y3), ", culoarea = ", im.getpixel((x3, y3)))
        #print(im.getpixel((x3, y3)) == (66,245,0))

        if pyautogui.pixelMatchesColor(1105, 155, (190,80,154), tolerance=50):
            print("stanga")
            pyautogui.keyDown('left')
            pyautogui.keyUp('left')
            #time.sleep(0.09)

        elif pyautogui.pixelMatchesColor(1263, 151, (2,255,250), tolerance=50):
            print("jos")
            pyautogui.keyDown('down')
            pyautogui.keyUp('down')
            #time.sleep(0.09)

        elif pyautogui.pixelMatchesColor(1425, 140, (18,251,10), tolerance=50):
            print("sus")
            pyautogui.keyDown('up')
            pyautogui.keyUp('up')
            #time.sleep(0.09)

        elif pyautogui.pixelMatchesColor(1580, 160, (243,67,61), tolerance=50):
            print("dreapta")
            pyautogui.keyDown('right')
            pyautogui.keyUp('right')
            #time.sleep(0.09)

        #elif im.getpixel((x3, y3)) is not (24, 19, 25):
        #    print(im.getpixel((x3, y3)))
        #else:
        #    print("??")

#mov = be509a (190,80,154)
#albastru = 47fcff (2,255,250)
#verde = 42f500 (18,251,10)
#rosu = f3433d (243,67,61)
#setari site: stanga = 1056, 380, jos = 1165, 387, sus = 1280, 375, dreapta = 1395, 382
