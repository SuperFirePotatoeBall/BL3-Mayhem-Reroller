import pyautogui
import pytesseract
from PIL import Image

def takeScreenShot(pos, name):
    #full: 1200, 420, 600, 500
    #1st: 1280, 470, 400, 30
    #2nd: 1280, 580, 400, 30
    #3rd: 1280, 695, 400, 30
    #4th: 1280, 810, 400, 40
    pyautogui.screenshot(name,region=pos)

def takeScreenShots():
    for i in range(len(screenShotDict)):
        takeScreenShot(screenShotDict[i+1][0], screenShotDict[i+1][1])


def getText(filePath):
    # Path to the Tesseract executable
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    # Extract text from the image
    extracted_text = extract_text_from_image(filePath)

    if extracted_text:
        return extracted_text
    else:
        print("Failed to extract text from the image.")

def extract_text_from_image(image_path):
    try:
        # Open the image file
        with Image.open(image_path) as img:
            # Use Tesseract to do OCR on the image
            extracted_text = pytesseract.image_to_string(img)
            return extracted_text
    except Exception as e:
        print("Error:", e)
        return None
    
def getModNames():
    modArray = []
    for i in range(len(screenShotDict)):
        mod = getText(screenShotDict[i+1][1])
        modArray.append(mod)
    return modArray

def removeNewLine(string):
    return string.replace('\n', '')

def removeAllNewLines(arr):
    newArr = []
    for i in arr:
        newStr = removeNewLine(i)
        newArr.append(newStr)
    return newArr


screenShotDict = {
        1: ((1280, 470, 400, 30), "1mod.png"),
        2: ((1280, 580, 400, 35), "2mod.png"),
        3: ((1280, 695, 400, 35), "3mod.png"),
        4: ((1280, 805, 400, 40), "4mod.png")
    }

takeScreenShots()
modNames = getModNames()
modNames = removeAllNewLines(modNames)
print(modNames)