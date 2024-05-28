def hello():
    print("hello")



def printcapteurs(my_marty):
    print("\nCapteur obstacle gauche : ",my_marty.get_obstacle_sensor_reading('left'))
    #ne capte des valeurs supérieur à 0 que à partir de genre 2cm

    print("\nCapteur obstacle droite : ",my_marty.get_obstacle_sensor_reading('right'))
    #ne capte des valeurs supérieur à 1 que à partir de genre 5cm


    #print("\nCapteur distance test : "+my_marty.get_distance_sensor())
    #Apparement le robot n'est pas doté d'un capteur de distance

    print("\nCapteur couleur : ",my_marty.get_ground_sensor_reading('left'))

    print("\nBatterie restante : ",my_marty.get_battery_remaining())
