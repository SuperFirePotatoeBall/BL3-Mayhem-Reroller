import pytesseract
from PIL import Image

class text():
    screenShotDict = {
            1: ((1280, 470, 400, 30), "1mod.png"),
            2: ((1280, 580, 400, 35), "2mod.png"),
            3: ((1280, 695, 400, 35), "3mod.png"),
            4: ((1280, 805, 400, 40), "4mod.png")
        }
    def __init__(self):
        pass

    def getText(self, filePath):
        # Path to the Tesseract executable
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

        # Extract text from the image
        extracted_text = self.extract_text_from_image(filePath)

        if extracted_text:
            return extracted_text
        else:
            print("Failed to extract text from the image.")

    def extract_text_from_image(self, image_path):
        try:
            # Open the image file
            with Image.open(image_path) as img:
                # Use Tesseract to do OCR on the image
                extracted_text = pytesseract.image_to_string(img)
                return extracted_text
        except Exception as e:
            print("Error:", e)
            return None
        
    def getModNames(self):
        modArray = []
        for i in range(len(self.screenShotDict)):
            mod = self.getText(self.screenShotDict[i+1][1])
            modArray.append(mod)
        modArray = self.removeAllNewLines(modArray)
        return modArray

    def removeNewLine(self, string):
        if string != None:
            return string.replace('\n', '')

    def removeAllNewLines(self, arr):
        newArr = []
        for i in arr:
            newStr = self.removeNewLine(i)
            newArr.append(newStr)
        return newArr