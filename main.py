from PyQt6.QtWidgets import QApplication
from ui.main_window import MainWindow
from models.gamepad import GameController
from functions.work_area_function import WorkAreaFunction
import threading

def start_game_controller(marty_ip):
    game_controller = GameController(marty_ip)
    game_controller.run()

if __name__ == "__main__":
    app = QApplication([])

    with open("style.qss", "r") as f:
        app.setStyleSheet(f.read())

    marty_ip = "192.168.0.101"  # Définissez l'adresse IP de Marty ici

    # Initialisez WorkAreaFunction avec la zone de travail
    work_area_function = WorkAreaFunction(None)
    work_area_function.set_marty_ip(marty_ip)

    # Créez la fenêtre principale et passez work_area_function
    window = MainWindow()
    window.show()

    # Démarrez le contrôleur de jeu dans un thread séparé pour ne pas bloquer l'UI
    game_controller_thread = threading.Thread(target=start_game_controller, args=(marty_ip,))
    game_controller_thread.daemon = True  # Permet de terminer le thread lorsque l'application se ferme
    game_controller_thread.start()

    app.exec()
