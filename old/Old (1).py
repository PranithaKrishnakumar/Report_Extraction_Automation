import cv2
import numpy as np
import pyautogui
import pytesseract
import re

#pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
def find_and_click_word(target_word):
    # Take a screenshot of the screen
    screenshot = pyautogui.screenshot()
    screenshot = np.array(screenshot)
    screenshot_gray = cv2.cvtColor(screenshot, cv2.COLOR_RGB2GRAY)

    # Perform OCR on the screenshot
    text = pytesseract.image_to_string(screenshot_gray)
    print(text)



    # Find the coordinates of the word in the text
    word_location = None
    if target_word.lower() in text.lower():
        indices = [(m.start(), m.end()) for m in re.finditer(target_word.lower(), text.lower())]
        for start, end in indices:
            word_location = (start, end)
            break

    # Perform a click on the word location
    if word_location:
        word_location_on_screen = pyautogui.locateOnScreen(target_word + ".png")
        if word_location_on_screen is not None:
            word_center = pyautogui.center(word_location_on_screen)
            pyautogui.click(word_center)

# Example usage:
target_word = "Terminal"
find_and_click_word(target_word)