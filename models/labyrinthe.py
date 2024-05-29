from martypy import Marty
import time

Red = 83  # Stop and celebrate
Blue = 34  # Slide left
Green = 30  # Forwards
Yellow = 96  # Backwards
Purple = 26  # Slide right


class Labyrinth:

    def __init__(self):
        self.current_direction = "forwards"
        self.reading = Green
        self.is_finished = False
        self.my_marty = None

    def read(self, foot):
        self.reading = self.my_marty.get_ground_sensor_reading(str(foot))

    def auto_walk(self, marty, foot_with_ground_sensor):
        self.my_marty = marty
        self.is_finished = False
        while not self.is_finished:
            try:
                print(self.current_direction)
                print(self.reading)
                self.read(str(foot_with_ground_sensor))
                if Red - 3 <= self.reading <= Red + 3:
                    self.my_marty.celebrate()
                    self.is_finished = True
                    self.current_direction = 'stopped'
                elif Blue - 1 <= self.reading <= Blue + 1:
                    self.my_marty.sidestep('left', 10, 35, 1000, None)
                    self.current_direction = 'left'
                elif Green - 1 <= self.reading <= Green + 1:
                    self.my_marty.walk(5, 'auto', 0, 35, 1500, None)
                    self.current_direction = 'forwards'
                elif Yellow - 3 <= self.reading <= Yellow + 3:
                    self.my_marty.walk(5, 'auto', 0, -35, 1500, None)
                    self.current_direction = 'backwards'
                elif Purple - 3 <= self.reading <= Purple + 3:
                    self.my_marty.sidestep('right', 10, 35, 1000, None)
                    self.current_direction = 'right'
                time.sleep(3)
            except:
                print("Could not get color")
                self.is_finished = True
