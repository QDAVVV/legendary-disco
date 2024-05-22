from __future__ import print_function
from martypy import Marty
import inputs


def game_controller():
    try:
        gamepad = inputs.devices.gamepads[0]
    except Exception:
        print("Could't find a proper controller.")

    gamepad.led = 1
    turning = False
    my_marty = None
    is_connected = False

    while True:
        events = inputs.get_gamepad()
        for event in events:
            if event.code == "BTN_THUMBR" and event.state == 1:
                if not is_connected:
                    print("Trying to connect...")
                    try:
                        my_marty = Marty("wifi", "192.168.0.101")
                        is_connected = True
                        print("Connection established !")
                        my_marty.stand_straight(1000, None)
                    except Exception:
                        print("Couldn't connect to Marty.")
                else:
                    print("Already connected !")

            if event.code == "BTN_THUMBL" and event.state == 1:
                print("BTN_THUMBL pressed.")

            if event.code == "BTN_SOUTH" and event.state == 1:
                if my_marty:
                    my_marty.dance()

            if event.code == "BTN_EAST" and event.state == 1:
                print("Reading color...")
                if my_marty:
                    try:
                        print(my_marty.get_obstacle_sensor_reading('left'))
                    except Exception as e:
                        print(e)
                else:
                    print("Marty not connected !")

            if event.code == "BTN_NORTH" and event.state == 1:
                print("X button pressed.")
                my_marty.stand_straight(1000, None)

            if event.code == "BTN_WEST" and event.state == 1:
                print("Y button released.")
                # my_marty.eyes('normal', 1000, None)

            if event.code == "ABS_HAT0Y" and event.state == -1:
                print("Going forwards.")
                if my_marty:
                    my_marty.walk(2, 'auto', 0, 35, 1500, None)

            if event.code == "ABS_HAT0Y" and event.state == 0:
                print("Stopped.")

            if event.code == "ABS_HAT0Y" and event.state == 1:
                print("Going backwards.")
                if my_marty:
                    my_marty.walk(2, 'auto', 0, -35, 1500, None)

            if event.code == "ABS_HAT0X" and event.state == 1:
                print("Going right.")
                if my_marty:
                    my_marty.sidestep('right', 2, 35, 1000, None)

            if event.code == "ABS_HAT0X" and event.state == -1:
                print("Going left.")
                if my_marty:
                    my_marty.sidestep('left', 2, 35, 1000, None)

            if event.code == "BTN_TR" and event.state == 1 and not turning:
                print("Turning right...")
                if my_marty:
                    my_marty.walk(2, 'auto', -15, 25, 1500, None)
                turning = True

            if event.code == "BTN_TR" and event.state == 0 and turning:
                print("Done turning.")
                turning = False

            if event.code == "BTN_TL" and event.state == 1 and not turning:
                print("Turning left...")
                if my_marty:
                    my_marty.walk(2, 'auto', 15, 25, 1500, None)
                turning = True

            if event.code == "BTN_TL" and event.state == 0 and turning:
                print("Done turning.")
                turning = False


if __name__ == "__main__":
    game_controller()
