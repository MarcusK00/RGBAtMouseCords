import pyautogui
import time
import keyboard
import threading
toggle = False

def toggleFunc():
    global toggle
    toggle = not toggle
    
def PrintPos():
    while True:
      global toggle
      x, y = pyautogui.position()
      pixel = pyautogui.pixel(x, y)
      print(f"Position: ({x}, {y}), Color: {pixel}", end="\r")
      time.sleep(0.1)
      keyboard.add_hotkey('c',toggleFunc)
      if(toggle):
        print(f"SAVED ## Position: ({x}, {y}), Color: {pixel}", end="\r")
        break

threading.Thread(target=PrintPos, daemon=True).start()
keyboard.wait('esc')