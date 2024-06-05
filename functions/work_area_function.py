from functions.marty_function import MartyFunction
from models.ip_manager import IPManager
class WorkAreaFunction:
    def __init__(self, work_area):
        self.work_area = work_area
        self.marty = None
        self.marty2 = None
        self.is_connected = False
        self.is_connected2 = False
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
        marty_ip = self.ip_manager.get_ip_address1()
        self.marty = MartyFunction(marty_ip)
        self.marty.connect()

        self.is_connected2 = True

        marty_ip2 = self.ip_manager.get_ip_address2()
        self.marty2 = MartyFunction(marty_ip2)
        self.marty2.connect()

        self.is_connected2 = True
        print(f"Connected to Marty at {marty_ip}")

    def up_clicked(self):
        
        if self.is_connected and self.marty:
            self.marty.walk(steps=8, direction='forward')
        else:
            print("Marty is not connected!")

    def down_clicked(self):
        if self.is_connected and self.marty:
            self.marty.walk(steps=8, direction='back')
        else:
            print("Marty is not connected!")


    def left_clicked(self):
        if self.is_connected and self.marty:
            self.marty.sidestep(direction='left')
        else:
            print("Marty is not connected!")

    def right_clicked(self):
        if self.is_connected and self.marty:
            self.marty.sidestep(direction='right')
        else:
            print("Marty is not connected!")

    def turn_left_clicked(self):
        if self.is_connected and self.marty:
            self.marty.turn(direction='left')
        else:
            print("Marty is not connected!")

    def turn_right_clicked(self):
        if self.is_connected and self.marty:
            self.marty.turn(direction='right')
        else:
            print("Marty is not connected!")
    
    def auto_clicked(self):
        if self.is_connected and self.marty:
            self.marty.auto_walk()
        else:
            print("Marty is not connected!")