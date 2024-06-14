from PyQt6.QtWidgets import QMainWindow, QGridLayout, QVBoxLayout, QWidget, QPushButton, QListWidgetItem
from PyQt6.QtGui import QDrag, QCursor, QIcon,QPen
from PyQt6.QtCore import Qt
from ui.work_area import WorkArea
from ui.block_list import BlockList
from blocks.for_block_item import ForBlockItem

from functions.blocklist_function import BlocklistFunction
from functions.work_area_function import WorkAreaFunction

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QProgressBar
from PyQt6.QtCore import QTimer
import random  # Pour simuler les niveaux de batterie aléatoires



class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Get Jinxed !")
        self.setGeometry(100, 100, 800, 600)
        self.work_area = WorkArea(self)

        self.work_area_function = WorkAreaFunction(self.work_area)
        self.blocklist_function = BlocklistFunction(self.work_area)
        self.block_list = BlockList(self.blocklist_function, parent=self.work_area)

        block_names = ["Connection", "For",  "Walk", "Dance", "Rotate", "SideStep",  "Wait","Auto"]

        for name in block_names:
            item = QListWidgetItem(name)
            self.block_list.addItem(item)

        button_names = ["On/Off", "Up", "Down", "Left", "Right", "Turn Left", "Turn Right","Auto"]
        button_layout = QVBoxLayout()

        for name in button_names:
            button = QPushButton(name)
            button_layout.addWidget(button)
            if name == "On/Off":
                button.clicked.connect(self.work_area_function.on_off_clicked)
            elif name == "Up":
                button.clicked.connect(self.work_area_function.up_clicked)
            elif name == "Down":
                button.clicked.connect(self.work_area_function.down_clicked)
            elif name == "Left":
                button.clicked.connect(self.work_area_function.left_clicked)
            elif name == "Right":
                button.clicked.connect(self.work_area_function.right_clicked)
            elif name == "Turn Left":
                button.clicked.connect(self.work_area_function.turn_left_clicked)
            elif name == "Turn Right":
                button.clicked.connect(self.work_area_function.turn_right_clicked)
            elif name == "Auto":
                button.clicked.connect(self.work_area_function.auto_clicked)
    


        main_layout = QGridLayout()
        main_layout.addWidget(self.block_list, 0, 0)
        main_layout.addWidget(self.work_area, 0, 1)
        main_layout.addLayout(button_layout, 0, 2)

        central_widget = QWidget()
        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)
        self.setWindowIcon(QIcon('hehehe'))
        self.setup_battery_indicator()

    def setup_battery_indicator(self):
        layout = QVBoxLayout(self)
        
        self.battery_indicator = QProgressBar(self)
        layout.addWidget(self.battery_indicator)
        layout.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Créer un minuteur pour mettre à jour l'indicateur de batterie périodiquement
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_battery_level)
        self.timer.start(1000)  # Mettre à jour toutes les 1000 ms (1 seconde)

    def update_battery_level(self):
        # Simuler la récupération du niveau de batterie (remplacer par votre propre logique)
        battery_level = random.randint(0, 100)
        
        # Mettre à jour l'indicateur de batterie (barre de progression)
        self.battery_indicator.setValue(battery_level)

    

    

    