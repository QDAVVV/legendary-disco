import msvcrt
import time
import threading
import sys
import martypy





class Application:
    Colors = []
    RegisteredIP = []
    LastIP= UnboundLocalError
    my_marty = UnboundLocalError
    Exit = False
    Marty_Controlled = False
    

    def Board_AvailableConnexionMethod(self):
        print("\n\nAvailable connexions: \n\n1- Wifi \n2- USB\n3- Quitter")
        input_ConnectionMethod = bytes.decode(msvcrt.getch(), encoding="utf-8")
        match input_ConnectionMethod:
            case '1':
                self.Board_WifiOptions()
            case '2':
                self.Board_USBOptions()
            case '3':
                sys.exit()
                
            case _:
                self.Board_AvailableConnexionMethod()
    
    def Board_USBOptions(self):
        print("\n\nBienvenue dans le panneau de configuration USB:\nVeuillez rentrer le port sur lequel est branché votre Marty\nNote USB port exemple: 'COM4'")
        a = input('Choisissez le port USB que vous souhaitez utiliser:\n')
        try:
            self.my_marty= martypy.Marty("USB", a)
        except Exception:
            print("Une erreur s'est produit lors de la connexion, retour vers l'ecran precedent !")
            self.Board_AvailableConnexionMethod()
        else: 
            print('Connected With success')
            self.Marty_Menu()


    def Board_WifiOptions(self):
        print("\n\nBienvenue dans le panneau de configuration du wifi: \n\n1- Connexion à partir d'une nouvelle addresse IP\n2- lister les options")
        Choosed = bytes.decode(msvcrt.getch(), encoding="utf-8")
        match Choosed:
            case '1':
                self.LastIP = input('Choisissez l\'addresse IP que vous souhaitez utiliser:\n')
                
                try:
                    self.my_marty = martypy.Marty("wifi", self.LastIP)
                except Exception:
                    print("Une erreur s'est produit lors de la connexion, retour vers l'ecran precedent !")
                    self.Board_WifiOptions()
                except:
                    print('quelque chose a mal tourne je sais juste pas quoi')
                else:
                    self.RegisteredIP.append(self.LastIP)
                    print('Connected With success')
                    self.Marty_Menu()

            case'2':
                print("Voici toute les addresses utilisés: ")
                for i in self.RegisteredIP:
                    print(i,": ",self.RegisteredIP[i])
                self.Board_WifiOptions()
            case _:
                self.Board_AvailableConnexionMethod()
                

    def Marty_Menu(self):
        print('Welcome To your Personal Marty, to move use the following letters\n\t\t\t  z\n\t\t\tq s d\nTo turn Left, press a\nTo turn right,press e\nTo ask a color read, press r\nTo enter Color Configuration Mode, press: o\nTo quit the program press "*"')

        self.MoveMarty()


    def MoveMarty(self):
        #a = 0
        self.Marty_Controlled = True
        while True:
            #time.sleep(a)
            print('Marty attend vos instructions !')
            try:
                input = bytes.decode(msvcrt.getch(), encoding="utf-8")
                
            except UnicodeDecodeError:
                print('Une erreur est survenue en lisant la valeur, la touche que vous vennez d\'appuyer n\'est pas définie !')
            match input:
                case 'z':
                    print("Marty is moving Forward")
                    self.my_marty.walk(2,'auto',0,25,1750,True)
                    #a = 1.750
                case 's':
                    print('Marty is moving Backward')
                    self.my_marty.walk(2,'auto',0,-25,1750,True)
                    #a = 1.750
                case 'e':
                    self.TournerDroite()
                case 'a':
                    self.TournerGauche()
                case 'q':
                    self.my_marty.sidestep('left',2,20,1250,True)
                case 'd':
                    self.my_marty.sidestep('right',2,20,1250,True)
                case'o':
                    self.Marty_Controlled = False
                    self.Board_ColorConfig()
                    break
                    
                case 'r':
                    self.ColorRead()
                    
                case '*':
                    self.Marty_Controlled = False
                    self.Exit = True
                    sys.exit()
    
    def Board_ColorConfig(self):
        print('\n\nWelcome to the Color Config Menu: \n1- Tableau des couleurs \n2- Ajouter une couleur\n3- Supprimer une couleur\n4- Quitter le Mode Configuration Couleur\n0- Tester le capteur de couleur')
        try:
            input = bytes.decode(msvcrt.getch(), encoding="utf-8")    
        except UnicodeDecodeError:
                print('Une erreur est survenue en lisant la valeur, la touche que vous vennez d\'appuyer n\'est pas définie !')
                self.Board_ColorConfig()
        match input:
            case '1':
                print(self.Colors)
                self.Board_ColorConfig()
            case '2':
                self.NewColor()
            case '0':
                self.ColorRead()
                self.Board_ColorConfig()
            case '4':
                self.MoveMarty()
            case _:
                self.Board_ColorConfig()

        

    def NewColor(self):
        input('Please enter the name of the color read')
    
    def TournerDroite(self):
            #1er pas
        self.my_marty.stand_straight()
        self.my_marty.lean('right',15,750,True)
        self.my_marty.lift_foot('left')
        self.my_marty.move_joint(1,10,500,True)
        self.my_marty.lower_foot('left')
            #2eme pas
        self.my_marty.lean('left',30,750,True)
        self.my_marty.lift_foot('right')
        self.my_marty.move_joint(4,10,500,True)
        self.my_marty.lower_foot('right')
        self.my_marty.stand_straight()
    
    def TournerGauche(self):
        #1er pas
        self.my_marty.stand_straight()
        self.my_marty.lean('left',15,750,True)
        self.my_marty.lift_foot('right')
        self.my_marty.move_joint(1,-10,500,True)
        self.my_marty.lower_foot('right')
            #2eme pas
        self.my_marty.lean('right',30,750,True)
        self.my_marty.lift_foot('left')
        self.my_marty.move_joint(4,-10,500,True)
        self.my_marty.lower_foot('left')
        self.my_marty.stand_straight()

    def ColorRead(self):
        Detect = self.my_marty.foot_on_ground('left')
        if Detect == True:
            print("Pied au sol ?: ",Detect,"\nvalue detected: ",self.my_marty.get_ground_sensor_reading('left'),"\nCouleur Detetcte: ", "\nCouleur en Hexa: ",self.my_marty.get_color_sensor_hex('left'),"\nCouleur en channel: ",self.my_marty.get_color_sensor_value_by_channel('left','clear'))
#print('Probleme avec un capteur: ', martypy.Exceptions.MartyCommandException)
            time.sleep(3)
            
                    
