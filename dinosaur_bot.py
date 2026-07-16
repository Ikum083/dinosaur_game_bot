import pyautogui as pya
import time as ti

class MainApp:
    def __init__(self):
        pya.FAILSAFE = True
        pya.PAUSE = 0.5
        self.screen_width, self.screen_height = pya.size()
        print(self.screen_width, self.screen_height)

        self.initial_area_x, self.initial_area_y = 1710, 400
        self.final_area_x, self.final_area_y = 1860, 490

        self.cactus_color_r, self.cactus_color_g, self.cactus_color_b = 106, 160, 69

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

if __name__ == "__main__":
    main = MainApp
    main.read_color()