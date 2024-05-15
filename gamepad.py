from __future__ import print_function
from martypy import Marty

import inputs

my_marty = Marty("wifi", "192.168.0.100")

gamepad = inputs.devices.gamepads[0]
turning = False

while True:
    events = inputs.get_gamepad()
    for event in events:
        if(event.code == "BTN_SOUTH" and event.state == 1):
            print("B button pressed.")
            my_marty.dance()

        if (event.code == "BTN_EAST" and event.state == 1):
            print("A button pressed.")
            try:
                my_marty.play_sound('no_way.mp3')
            except:
                print("Couldn't play sound.")

        if (event.code == "BTN_NORTH" and event.state == 1):
            print("X button pressed.")
            #my_marty.eyes('angry', 1000, None)

        if (event.code == "BTN_WEST" and event.state == 1):
            print("Y button released.")
            #my_marty.eyes('normal', 1000, None)

        if (event.code == "ABS_HAT0Y" and event.state == -1):
            print("Going forwards.")
            my_marty.walk(2, 'auto', 0, 25, 1500, None)

        if (event.code == "ABS_HAT0Y" and event.state == 0):
            print("Stopped.")

        if (event.code == "ABS_HAT0X" and event.state == 1):
            print("Going right.")
            my_marty.sidestep('right', 2, 35, 1000, None)
        if (event.code == "ABS_HAT0X" and event.state == -1):
            print("Going left.")
            my_marty.sidestep('left', 2, 35, 1000, None)

        if (event.code == "BTN_TR" and event.state == 1 and not turning):
            print("Turning right...")
            my_marty.walk(2, 'auto', -10, 25, 1500, None)
            turning = True
        if (event.code == "BTN_TR" and event.state == 0 and turning):
            print("Done turning.")
            turning = False

        if (event.code == "BTN_TL" and event.state == 1 and not turning):
            print("Turning left...")
            my_marty.walk(2, 'auto', 10, 25, 1500, None)
            turning = True
        if (event.code == "BTN_TL" and event.state == 0 and turning):
            print("Done turning.")
            turning = False


