import pyautogui
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
def click_on_word(word):
    try:
        while True:
            screenshot = pyautogui.screenshot()
            if word.lower() in pytesseract.image_to_string(screenshot).lower():
                position = pyautogui.locateOnScreen('screenshot.png', confidence=0.8)
                if position is not None:
                    center_x, center_y, _, _ = pyautogui.center(position)
                    pyautogui.click(center_x, center_y)
                    break
    except KeyboardInterrupt:
        print("Program stopped by the user.")

word_to_find = input("Enter the word to find: ")
click_on_word(word_to_find)
