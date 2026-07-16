import pyautogui as pya
import time as ti
import threading as thr

class MainApp:
    def __init__(self):
        pya.FAILSAFE = True
        pya.PAUSE = 0.5

        self.initial_area_x, self.initial_area_y = 1060, 380
        self.final_area_x, self.final_area_y = 1880, 490

        self.cactus_color_r, self.cactus_color_g, self.cactus_color_b = 106, 160, 69

        self.region = (self.initial_area_x, self.initial_area_y, (self.final_area_x - self.initial_area_x), (self.final_area_y - self.initial_area_y))

        self.screenshot = None

        self.lock = thr.Lock()
        
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

    def screenshot_screen(self, stop_flag):
        while not stop_flag.is_set():
            shot = pya.screenshot(region=self.region)
            shot.save('region_captured.png')
            with self.lock:
                self.screenshot = shot
            ti.sleep(0.03)

    def detect_cactus(self, images, stop_flag):
        last_jump_time = 0
        cooldown = 0.1
        jump_threshold_x = 30

        while not stop_flag.is_set():
            with self.lock:
                current_shot = self.screenshot

            if current_shot is not None and (ti.time() - last_jump_time > cooldown):
                closest_match = None
                for image in images:
                    try:
                        locate = pya.locate(image, current_shot, confidence=0.4)
                        if locate:
                            if closest_match is None or locate.left < closest_match.left:
                                closest_match = locate
                    except pya.ImageNotFoundException:
                        continue

                if closest_match and closest_match.left <= jump_threshold_x:
                    print(f"Jumping — cactus at left={closest_match.left}")
                    pya.press('space')
                    last_jump_time = ti.time()

            ti.sleep(0.03) 

if __name__ == "__main__":
    main = MainApp()

    stop_flag = thr.Event()

    image_list = ['cactus.png','cactus_2.png','cactus_3.png','cactus_4.png']

    thread_1 = thr.Thread(target = main.screenshot_screen, args = (stop_flag,), daemon = True)
    thread_2 = thr.Thread(target = main.detect_cactus, args = (image_list, stop_flag), daemon = True)
    
    thread_1.start()
    thread_2.start()
    
    try:
        while True:
            ti.sleep(0.01)
    except KeyboardInterrupt:
        stop_flag.set()
        thread_1.join()
        thread_2.join()

