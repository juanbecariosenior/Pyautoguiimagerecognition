import pyautogui
import time

time.sleep(3)
#pyautogui.displayMousePosition()
iml = pyautogui.screenshot(region=(764,354,385,495))
iml.save(r"C:\Users\Becario\Desktop\pyautogui\tercer videotutorial\savedimage.png")
