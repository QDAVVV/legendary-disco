from __future__ import print_function

import inputs

gamepad = inputs.devices.gamepads[0]
turning = False

while True:
    events = inputs.get_gamepad()
    for event in events:
        if(event.code == "BTN_SOUTH" and event.state == 1):
            print("B button pressed.")
        if (event.code == "BTN_EAST" and event.state == 1):
            print("A button released.")
        if (event.code == "BTN_NORTH" and event.state == 1):
            print("X button pressed.")
        if (event.code == "BTN_WEST" and event.state == 1):
            print("Y button released.")

        if (event.code == "ABS_HAT0Y" and event.state == 1):
            print("Going backwards.")
        if (event.code == "ABS_HAT0Y" and event.state == -1):
            print("Going forwards.")

        if (event.code == "ABS_HAT0Y" and event.state == 0):
            print("Stopped.")


        if (event.code == "BTN_TR" and event.state == 1 and not turning):
            print("Turning right...")
            turning = True
        if (event.code == "BTN_TR" and event.state == 0 and turning):
            print("Done turning.")
            turning = False

        if (event.code == "BTN_TL" and event.state == 1 and not turning):
            print("Turning left...")
            turning = True
        if (event.code == "BTN_TL" and event.state == 0 and turning):
            print("Done turning.")
            turning = False


