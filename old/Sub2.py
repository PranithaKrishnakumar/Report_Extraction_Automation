import cv2
import numpy as np
import pyautogui

def click_on_word(target_word):
    # Take a screenshot of the screen
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)
    #print(screenshot_gray)

    # Load the word template image
    template = cv2.imread(r"E:\Github\Report_Extraction_Automation\a.PNG", 0)  # Replace with your own word template image
    #print(template)

    # Perform template matching
    result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.85  # Adjust as needed
    locations = np.where(result >= threshold)
    #print(zip(*locations[::-1]))

    for loc in zip(*locations[::-1]):
        top_left = loc
        bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])
        #print(bottom_right)
        word_location = pyautogui.center((top_left[0], top_left[1], bottom_right[0], bottom_right[1]))
        pyautogui.click(word_location)
        print(word_location)

# Example usage:
target_word = ' Go '
click_on_word(target_word)
