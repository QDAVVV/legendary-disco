import Marty

class Donnees() :

    acceleration = self.marty.get_accelerometer()
    is_moving = self.marty.is_moving()
    is_paused = self.marty.is_paused()
    is_blocking = self.marty.is_blocking()
    distance = self.marty.get_distance_sensor()
    obstacle = self.marty.get_obtacle_sensor_reading()
    battery = self.marty.get_battery_remaining()



    def __init__(self, marty) :
        self.marty = martyy


    def showData(self):
        print("test")

    def update(self):
        self.acceleration = self.marty.get_accelerometer()
        self.is_moving = self.marty.is_moving()
        self.is_paused = self.marty.is_paused()
        self.is_blocking = self.marty.is_blocking()
        self.distance = self.marty.get_distance_sensor()
        self.obstacle = self.marty.get_obtacle_sensor_reading()

    
