import pyautogui
import time

print("Mouse jiggler started. Press CTRL + C to stop.")

try:
    while True:
        # get current position
        x, y = pyautogui.position()
        
        # move slightly right
        pyautogui.moveTo(x + 500, y, duration=0.2)
        time.sleep(2)

        # move back to original
        pyautogui.moveTo(x, y, duration=0.2)
        time.sleep(2)

except KeyboardInterrupt:
    print("Stopped by user.")
