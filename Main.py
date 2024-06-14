import martypy

from Definitions import *

global chaos;

print("\nWelcome to my script, where madness is everywhere and chaos is the only constant !\nTo start follow the menu.")
App = Application()


App.Board_AvailableConnexionMethod()

#t = threading.Thread(target=ColorRead)
#t.daemon = True
#t.start()

while App.Exit == False:
    time.sleep(1)

#    try:
#        inp = bytes.decode(msvcrt.getch(), encoding="utf-8")
#    except UnicodeDecodeError:
#        print('Une erreur est survenue en lisant la valeur, la touche que vous vennez d\'appuyer n\'est pas définie !')
#    handling_input(inp)
#    match inp:
#        case'a':
#            print('quitting')
#            sys.exit()
