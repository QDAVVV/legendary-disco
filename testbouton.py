import inputs

def game_controller():
    try:
        gamepad = inputs.devices.gamepads[0]
    except Exception:
        print("Could't find a proper controller.")

    gamepad.led = 1 # Ne sert a rien mais faut pas le supprimer

    while True:
        events = inputs.get_gamepad()
        for event in events:
            print(event.code)
            

if __name__ == "__main__":
    game_controller()