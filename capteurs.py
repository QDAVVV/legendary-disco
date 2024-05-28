from martypy import Marty


class Capteurs():


    couleur = 0
    obstacle = 0
    batterie = 101

    def __init__(self, my_martyy) :
        self.my_marty = my_martyy

    def actualiserCapteurs(self, my_marty):
        self.couleur = my_marty.get_ground_sensor_reading('left')
        self.obstacle = my_marty.get_obstacle_sensor_reading('right')
        self.batterie = my_marty.get_battery_remaining()

    def getCouleur(self):
        return self.couleur

    def getObstacle(self):
        return self.obstacle
    
    def getBatterie(self):
        return self.batterie


    #     print("\nCapteur obstacle gauche : ",my_marty.get_obstacle_sensor_reading('left'))
    # #ne capte des valeurs supérieur à 0 que à partir de genre 2cm

    #     print("\nCapteur obstacle droite : ",my_marty.get_obstacle_sensor_reading('right'))
    # #ne capte des valeurs supérieur à 1 que à partir de genre 5cm


    # #print("\nCapteur distance test : "+my_marty.get_distance_sensor())
    # #Apparement le robot n'est pas doté d'un capteur de distance

    #     print("\nCapteur couleur : ",my_marty.get_ground_sensor_reading('left'))

    #     print("\nBatterie restante : ",my_marty.get_battery_remaining())
