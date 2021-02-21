import webbrowser
import time

from pynput.keyboard import Controller,Key
keyboard = Controller()
new=2
url="https://meet.google.com/xoz-qvfx-apw"
webbrowser.open(url, new=new)
time.sleep(3)
a = 1
while a < 10:
    keyboard.press(Key.tab)
    time.sleep(0.2)
    keyboard.release(Key.tab)
    time.sleep(0.2)
    a = a + 1

keyboard.press(Key.enter)
time.sleep(0.2)
keyboard.release(Key.enter)
print ("in the meeting")
keyboard.press(Key.tab)
time.sleep(0.2)
keyboard.release(Key.tab)
keyboard.press(Key.tab)
time.sleep(0.2)
keyboard.release(Key.tab)
time.sleep(0.2)
keyboard.press(Key.enter)
time.sleep(0.2)
keyboard.release(Key.enter)
time.sleep(1)
keyboard.type('here')
keyboard.press(Key.enter)
time.sleep(0.2)
keyboard.release(Key.enter)

