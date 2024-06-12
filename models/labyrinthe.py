from martypy import Marty
import time


class Labyrinth:

    def __init__(self):
        self.current_direction = "forwards"
        self.reading = 0
        self.is_finished = False
        self.my_marty = None
        self.directions = []

        self.Red = 0  # arrivée
        self.Cyan = 0  # départ
        self.Green = 0  # nord
        self.Yellow = 0  # sud
        self.Blue = 0  # est
        self.Rose = 0  # ouest

    def read(self, foot):
        if self.my_marty:
            self.reading = self.my_marty.get_ground_sensor_reading(str(foot))
        else:
            print("Marty is not connected!")
        

    def calibrate_color(self, color_name):
        print(f"Please place Marty on {color_name} card.")
        time.sleep(3)
        self.read("left")
        setattr(self, color_name, self.reading)
        print(f"{color_name}: {self.reading}")

    def calibrate(self):
        colors = ["Cyan", "Red", "Green", "Yellow", "Blue", "Rose"]
        for color in colors:
            self.calibrate_color(color)
        print("Calibrating done!")

    def join_directions(self, other_martys_directions):
        self.directions.extend(other_martys_directions)

    def get_measure(self, direction, marty_instance):
        marty_instance.stand_straight(1000, None)
        
        self.read("left", 20)
        direction.append(self.reading)

    def recon(self,marty_instance):
        directions = []
    
        marty_instance.stand_straight(1000, None)
        print("Recon started.")
        self.get_measure(directions, marty_instance)  # Passer l'instance de Marty à get_measure
        print("Function 1 done.")
        print(directions)
        

        for _ in range(2):
            self.my_marty.walk(5, 'auto', 0, 35, 1500, None)
            self.read("left", 20)
            directions.append(self.reading)
            print(directions)

        self.my_marty.stand_straight(1000, None)
        self.my_marty.sidestep('right', 5, 35, 1000, None)
        self.read("left", 20)
        directions.append(self.reading)
        print(directions)

        for _ in range(2):
            self.my_marty.walk(5, 'auto', 0, -35, 1500, None)
            self.read("left", 20)
            directions.append(self.reading)
            print(directions)

        self.my_marty.stand_straight(1000, None)
        self.my_marty.sidestep('right', 5, 35, 1000, None)
        self.read("left", 20)
        directions.append(self.reading)
        print(directions)

        for _ in range(2):
            self.my_marty.walk(5, 'auto', 0, 35, 1500, None)
            self.read("left", 20)
            directions.append(self.reading)
            print(directions)
            

        print("Recon over.")
        print(directions)
        filtered_directions = []

        for direction in directions:
            for color in ["Blue", "Red", "Green", "Cyan", "Yellow", "Rose"]:
                if getattr(self, color) - 5 <= direction <= getattr(self, color) + 5:
                    filtered_directions.append(direction)

        self.directions = filtered_directions
        print(self.directions)

    

    def auto_walk(self, marty, foot_with_ground_sensor):
        self.my_marty = marty
        self.is_finished = False
        while not self.is_finished:
            try:
                print(self.current_direction)
                print(self.reading)
                self.read(str(foot_with_ground_sensor), 20)
                if self.Red - 5 <= self.reading <= self.Red + 5:
                    self.my_marty.celebrate()
                    self.is_finished = True
                    self.current_direction = 'stopped'
                elif self.Blue - 5 <= self.reading <= self.Blue + 5:
                    self.my_marty.sidestep('left', 10, 35, 1000, None)
                    self.current_direction = 'left'
                elif self.Green - 5 <= self.reading <= self.Green + 5:
                    self.my_marty.walk(5, 'auto', 0, 35, 1500, None)
                    self.current_direction = 'forwards'
                elif self.Yellow - 5 <= self.reading <= self.Yellow + 5:
                    self.my_marty.walk(5, 'auto', 0, -35, 1500, None)
                    self.current_direction = 'backwards'
                elif self.Cyan - 5 <= self.reading <= self.Cyan + 5:
                    self.my_marty.sidestep('right', 10, 35, 1000, None)
                    self.current_direction = 'right'
                time.sleep(3)
            except Exception:
                print("Could not get color")
                self.is_finished = True

    def walk_through_labyrinth(self):
        for direction in self.directions:
            if self.Red - 5 <= direction <= self.Red + 5:
                self.my_marty.celebrate()
                self.is_finished = True
                self.current_direction = 'stopped'
            elif self.Blue - 5 <= direction <= self.Blue + 5:
                self.my_marty.sidestep('right', 10, 35, 1000, None)
                self.current_direction = 'right'
            elif self.Green - 5 <= direction <= self.Green + 5:
                self.my_marty.walk(5, 'auto', 0, 35, 1500, None)
                self.current_direction = 'forwards'
            elif self.Yellow - 5 <= direction <= self.Yellow + 5:
                self.my_marty.walk(5, 'auto', 0, -35, 1500, None)
                self.current_direction = 'backwards'
            elif self.Rose - 5 <= direction <= self.Rose + 5:
                self.my_marty.sidestep('left', 10, 35, 1000, None)
                self.current_direction = 'left'
            elif self.Cyan - 5 <= direction <= self.Cyan + 5:
                self.my_marty.stand_straight(1000, None)
            time.sleep(3)
