import pyautogui as pya
import time as ti
import os

class MainApp:
    def __init__(self):
        pya.FAILSAFE = True
        pya.PAUSE = 0.5

        self.initial_area_x, self.initial_area_y = 1710, 400
        self.final_area_x, self.final_area_y = 1860, 490

        self.cactus_color_r, self.cactus_color_g, self.cactus_color_b = 106, 160, 69

        self.region = (self.initial_area_x, self.initial_area_y, (self.final_area_x - self.initial_area_x), (self.final_area_y - self.initial_area_y))

        pya.moveTo(1300, 400, duration = 0.1)

        pya.click()

    def read_position():
        reading = True
        while reading:
            print(f"Mouse position: {pya.position()}")

    def read_color():
        coloring = True
        while coloring:
            position_x, position_y = pya.position()
            pixel_color = pya.pixel(position_x, position_y)
            print(f"Mouse color at: {pixel_color}")

    def detect_cactus(self, images):
        screenshot = pya.screenshot(region = self.region)
        screenshot.save('region_captured.png')

        for image in images:
            try:
                locate = pya.locate(image, screenshot, confidence = 0.6)
                if locate:
                    print("Cactus!")
                    ti.sleep(1.5)
                    pya.press('space')
                    ti.sleep(0.1)
                    pya.press('down')
            except pya.ImageNotFoundException:
                continue

if __name__ == "__main__":
    main = MainApp()
    image_list = ['cactus.png','cactus_2.png','cactus_3.png','cactus_4.png']
    while True:
            main.detect_cactus(image_list)
