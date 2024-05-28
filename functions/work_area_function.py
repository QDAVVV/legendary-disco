from functions.marty_function import MartyFunction
from models.ip_manager import IPManager
class WorkAreaFunction:
    def __init__(self, work_area):
        self.work_area = work_area
        self.marty = None
        self.is_connected = False
        self.ip_manager = IPManager.get_instance()

    def set_marty_ip(self, marty_ip):
        self.marty_ip = marty_ip
    
    
    def execute_program(self):
        work_area = self.work_area
        blocks = work_area.get_widgets()
        print(f"Nombre de blocs dans la zone de travail : {len(blocks)}")
        connections = work_area.get_connections()
        print(f"Nombre de connexions dans la zone de travail : {len(connections)}")

    def organize_blocks_and_execute(self):
        work_area = self.work_area
        work_area.organize_blocks_for_execution()

    def on_off_clicked(self):
        marty_ip = self.ip_manager.get_ip_address()
        self.marty = MartyFunction(marty_ip)
        self.is_connected = True
        print(f"Connected to Marty at {marty_ip}")

    def up_clicked(self):
        print("Le bouton 'Up' a été cliqué!")
        if self.is_connected and self.marty_function:
            self.marty_function.walk(steps=2, direction='forward')  # Faites avancer Marty de deux pas devant lui
        else:
            print("Marty is not connected!")

    def down_clicked(self):
        print("Le bouton 'Down' a été cliqué!")

    def left_clicked(self):
        print("Le bouton 'Left' a été cliqué!")

    def right_clicked(self):
        print("Le bouton 'Right' a été cliqué!")

    def turn_left_clicked(self):
        print("Le bouton 'Turn Left' a été cliqué!")

    def turn_right_clicked(self):
        print("Le bouton 'Turn Right' a été cliqué!")