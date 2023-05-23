import pyautogui
import time

def Report_Finder(tag):
    try:
        position = pyautogui.locateOnScreen(f"E:\Github\Report_Extraction_Automation\pics\{tag}.PNG", confidence=0.8)
        relative_position = pyautogui.center(position)
        button_X, button_Y = relative_position
        #print(button_X, button_Y)
        pyautogui.click(button_X, button_Y)
        print("Passed")
        time.sleep(10)
    
    except:
        print("Failed")

