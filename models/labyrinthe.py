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
        self.directions = []

    def read(self, foot):
        self.reading = self.my_marty.get_ground_sensor_reading(str(foot))

    def join_directions(self, other_martys_directions):
        for i in range(len(other_martys_directions)):
            self.directions.append(other_martys_directions[i])

    def recon(self):
        directions = []

        for _ in range(3):
            self.my_marty.walk(5, 'auto', 0, 35, 1500, None)
            self.read("left")
            directions.append(self.reading)

        self.my_marty.sidestep('right', 10, 35, 1000, None)
        self.read("left")
        directions.append(self.reading)

        for _ in range(2):
            self.my_marty.walk(5, 'auto', 0, -35, 1500, None)
            self.read("left")
            directions.append(self.reading)

        self.my_marty.sidestep('right', 10, 35, 1000, None)
        self.read("left")
        directions.append(self.reading)

        for _ in range(2):
            self.my_marty.walk(5, 'auto', 0, 35, 1500, None)
            self.read("left")
            directions.append(self.reading)

        for i in range(5):
            print("Second recon beginning in " + str(5 - i) + ".")
            time.sleep(1)


        print("Recon over.")

        filtered_directions = [direction for direction in directions if
                               Blue - 1 <= direction <= Blue + 1
                               or Red - 1 <= direction <= Red + 1
                               or Green - 1 <= direction <= Green + 1]

        self.directions = filtered_directions

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

    def walk_through_labyrinth(self):
        for i in range(len(self.directions)):
            if Red <= self.directions[i] <= Red:
                self.my_marty.celebrate()
                self.is_finished = True
                self.current_direction = 'stopped'
            elif Blue <= self.directions[i] <= Blue:
                self.my_marty.sidestep('left', 10, 35, 1000, None)
                self.current_direction = 'left'
            elif Green <= self.directions[i] <= Green:
                self.my_marty.walk(5, 'auto', 0, 35, 1500, None)
                self.current_direction = 'forwards'
            elif Yellow <= self.directions[i] <= Yellow:
                self.my_marty.walk(5, 'auto', 0, -35, 1500, None)
                self.current_direction = 'backwards'
            elif Purple <= self.directions[i] <= Purple:
                self.my_marty.sidestep('right', 10, 35, 1000, None)
                self.current_direction = 'right'
            time.sleep(3)
