import pyautogui

class screenShot():
    def __init__(self):
        pass

    screenShotDict = {
        1: ((1280, 470, 400, 35), "1mod.png"),
        2: ((1280, 580, 400, 35), "2mod.png"),
        3: ((1280, 695, 400, 35), "3mod.png"),
        4: ((1280, 805, 400, 40), "4mod.png")
    }

    def takeScreenShot(self, pos, name):  # Removed `self` from the arguments
        pyautogui.screenshot(name, region=pos)

    def takeScreenShots(self):
        for key in self.screenShotDict:
            pos, name = self.screenShotDict[key]  # Unpack the tuple
            self.takeScreenShot(pos, name)  # Call the method without passing `self`


