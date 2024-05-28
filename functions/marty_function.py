from martypy import Marty

class MartyFunction:
    def __init__(self, marty_ip):
        self.marty_ip = marty_ip
        self.my_marty = None

    def dance(self):
        """Make Marty dance."""
        self.my_marty.dance()

    def connect(self):
        """Connect to Marty"""
        self.my_marty = Marty("wifi", self.marty_ip)
        self.my_marty.stand_straight(1000, None)

    def stand_straight(self):
        """Make Marty stand straight."""
        self.my_marty.stand_straight(1000, None)

    def read_color(self):
        """Read color from Marty's obstacle sensor."""
        try:
            return self.my_marty.get_obstacle_sensor_reading('left')
        except Exception as e:
            print(f"Error reading color: {e}")
            return None

    def walk(self, steps=2, direction='auto', turn=0, step_length=35, step_time=1500):
        """Make Marty walk."""
        if self.my_marty:
            self.my_marty.walk(steps, direction, turn, step_length, step_time, None)
        else:
            print("Marty is not connected")

    def sidestep(self, direction='right', steps=2, step_length=35, step_time=1000):
        """Make Marty sidestep."""
        self.my_marty.sidestep(direction, steps, step_length, step_time, None)

    def turn(self, direction='right', steps=2, turn_amount=25, step_time=1500):
        """Make Marty turn."""
        if direction == 'right':
            self.my_marty.walk(steps, 'auto', -15, turn_amount, step_time, None)
        else:
            self.my_marty.walk(steps, 'auto', 15, turn_amount, step_time, None)