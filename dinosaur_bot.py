import pyautogui as pya
import time as ti

class MainApp:
    def __init__(self):
        pya.FAILSAFE = True
        pya.PAUSE = 0.5
        self.screen_width, self.screen_height = pya.size()
        print(self.screen_width, self.screen_height)

        pya.moveTo(100, 100, duration = 1)

        pya.click()

if __name__ == "__main__":
    main = MainApp
    main()