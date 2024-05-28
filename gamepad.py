from __future__ import print_function
from martypy import Marty
import inputs
from labyrinthe import Labyrinth


IP = "192.168.0.104"


def game_controller():
    try:
        gamepad = inputs.devices.gamepads[0]
    except Exception:
        print("Could't find a proper controller.")

    gamepad.led = 1 # Ne sert a rien mais faut pas le supprimer
    turning = False
    my_marty = None
    is_connected = False

    labyrinth = Labyrinth()

    while True:
        events = inputs.get_gamepad()
        for event in events:
            if event.code == "BTN_THUMBR" and event.state == 1: # Appuyer sur joystick droit pour se connecter.
                if not is_connected:
                    print("Trying to connect...")
                    try:
                        my_marty = Marty("wifi", IP)
                        is_connected = True
                        print("Connection established !")
                        my_marty.stand_straight(1000, None)
                    except Exception as e:
                        print("Couldn't connect to Marty.")
                else:
                    print("Already connected !")

            if event.code == "BTN_THUMBL" and event.state == 1:
                print("BTN_THUMBL pressed.")
                labyrinth.auto_walk(my_marty, 'left')

            if event.code == "BTN_SOUTH" and event.state == 1: # Bouton B(bouton du bas) = dance
                print("B button pressed.")
                if my_marty:
                    my_marty.dance()

            if event.code == "BTN_EAST" and event.state == 1: #Bouton A(bouton de droite) = read color
                print("Reading color...")
                # Red = 113
                # Blue = 42
                # Green = 39
                # Yellow = 126
                # Purple = 35
                if my_marty:
                    try:
                        print(my_marty.get_ground_sensor_reading('left'))
                    except Exception as e:
                        print(e)
                else:
                    print("Marty not connected !")

            if event.code == "BTN_NORTH" and event.state == 1: # Bouton X(bouton du haut) = se met droit
                print("X button pressed.")
                if my_marty:
                    my_marty.stand_straight(1000, None)

            if event.code == "BTN_WEST" and event.state == 1:
                print("Y button released.")
                my_marty.eyes('angry', 1000, None)
                my_marty.eyes('normal', 1000, None)

            if event.code == "ABS_HAT0Y" and event.state == -1: # Pad directionnel
                print("Going forwards.")
                if my_marty:
                    my_marty.walk(2, 'auto', 0, 35, 1500, None)

            if event.code == "ABS_HAT0Y" and event.state == 0:
                print("Stopped.")

            if event.code == "ABS_HAT0Y" and event.state == 1: # Pad directionnel
                print("Going backwards.")
                if my_marty:
                    my_marty.walk(2, 'auto', 0, -35, 1500, None)

            if event.code == "ABS_HAT0X" and event.state == 1: # Pad directionnel
                print("Going right.")
                if my_marty:
                    my_marty.sidestep('right', 2, 35, 1000, None)

            if event.code == "ABS_HAT0X" and event.state == -1: # Pad directionnel
                print("Going left.")
                if my_marty:
                    my_marty.sidestep('left', 2, 35, 1000, None)

            if event.code == "BTN_TR" and event.state == 1 and not turning: # Petite gachette droite = rotation a droite
                print("Turning right...")
                if my_marty:
                    my_marty.walk(2, 'auto', -15, 25, 1500, None)
                turning = True

            if event.code == "BTN_TR" and event.state == 0 and turning:
                print("Done turning.")
                turning = False

            if event.code == "BTN_TL" and event.state == 1 and not turning: # Petite gachette gauche = rotation a gauche
                print("Turning left...")
                if my_marty:
                    my_marty.walk(2, 'auto', 15, 25, 1500, None)
                turning = True

            if event.code == "BTN_TL" and event.state == 0 and turning:
                print("Done turning.")
                turning = False


if __name__ == "__main__":
    game_controller()
