from PyQt6.QtWidgets import QApplication, QMainWindow,QGridLayout, QPushButton, QVBoxLayout, QWidget, QListWidget, QListWidgetItem, QGraphicsTextItem, QGraphicsScene, QGraphicsView, QGraphicsItem,QGraphicsRectItem,QGraphicsWidget, QGraphicsProxyWidget,QGraphicsEllipseItem, QGraphicsLineItem
from PyQt6.QtCore import Qt, QMimeData, QRectF, QPoint
from PyQt6.QtGui import QDrag, QCursor, QIcon,QPen

from design import ForBlockWidget, WhileBlockWidget, WalkBlockWidget


class ForBlockItem(QGraphicsProxyWidget):
    def __init__(self, x, y, width, height, work_area):
        super().__init__()
        self.setGeometry(QRectF(x, y, width, height))
        self.work_area = work_area
        self.for_block = ForBlockWidget()
        
         # Create a QGraphicsView
        view = QGraphicsView()
        
        # Set the scene of the QGraphicsView to the scene
        scene = QGraphicsScene()
        scene.addItem(self.for_block)

        view.setScene(scene)
        

        # Now you can add the QGraphicsView to your main widget
        self.setWidget(view)

        # Passer les événements de souris aux points de connexion
        for point in self.for_block.input_connection_points:
            point.setParentItem(self)
        for point in self.for_block.output_connection_points:
            point.setParentItem(self)

        # Activer la réception des événements de survol
        self.setAcceptHoverEvents(True)
    
        
class WhileBlockItem(QGraphicsProxyWidget):
    def __init__(self, x, y, width, height, work_area):
        super().__init__()
        self.setGeometry(QRectF(x, y, width, height))
        self.work_area = work_area
        self.while_block = WhileBlockWidget()
        
         # Create a QGraphicsView
        view = QGraphicsView()

        # Set the scene of the QGraphicsView to the scene
        scene = QGraphicsScene()
        scene.addItem(self.while_block)
        view.setScene(scene)

        # Now you can add the QGraphicsView to your main widget
        self.setWidget(view)
        
class WalkBlockItem(QGraphicsProxyWidget):
    def __init__(self, x, y, width, height, work_area):
        super().__init__()
        self.setGeometry(QRectF(x, y, width, height))
        self.work_area = work_area
        self.walk_block = WalkBlockWidget()
        
         # Create a QGraphicsView
        view = QGraphicsView()

        # Set the scene of the QGraphicsView to the scene
        scene = QGraphicsScene()
        scene.addItem(self.walk_block)
        view.setScene(scene)

        # Now you can add the QGraphicsView to your main widget
        self.setWidget(view)

#Initialisation de la class BlockList
class BlockList(QListWidget):
    """
    A custom QListWidget subclass that allows dragging items.
    """

    def __init__(self, parent=None):
        """
        Initializes the BlockList.

        Args:
            parent: The parent widget (default: None).
        """
        super().__init__(parent)
        self.setDragEnabled(True)
        
        

    def startDrag(self, event):
        """
        Starts the drag operation.

        Args:
            actions: The drag actions.

        Returns:
            None
        """
        block_type = self.currentItem().text()
        mouse_position = QCursor.pos()

        if block_type == "For":
            x, y = mouse_position.x(), mouse_position.y()
            width, height = 200, 100  # Replace with actual values
            work_area = None  # Replace with actual work area
            block = ForBlockItem(x, y, width, height, work_area)
            
            
        
        elif block_type == "While":
            x, y = mouse_position.x(), mouse_position.y()
            width, height = 100, 100
            work_area = None
            block = WhileBlockItem(x, y, width, height, work_area)
            print("While")
        
        elif block_type == "Walk":
            x, y = mouse_position.x(), mouse_position.y()
            width, height = 100, 100
            work_area = None
            block = WalkBlockItem(x, y, width, height, work_area)
            print("Walk")

        drag = QDrag(self)
        mime_data = QMimeData()
        mime_data.setText(block_type)
        drag.setMimeData(mime_data)
        drag.exec()

class ConnectionManager:
    def __init__(self):
        self.connections = []

    def add_connection(self, start_block, end_block):
        """
        Add a connection between two blocks.

        Args:
            start_block: The block where the connection starts.
            end_block: The block where the connection ends.
        """
        self.connections.append((start_block, end_block))

    def remove_connection(self, start_block, end_block):
        """
        Remove a connection between two blocks.

        Args:
            start_block: The block where the connection starts.
            end_block: The block where the connection ends.
        """
        if (start_block, end_block) in self.connections:
            self.connections.remove((start_block, end_block))

    def has_connection(self, start_block, end_block):
        """
        Check if there is a connection between two blocks.

        Args:
            start_block: The block where the connection starts.
            end_block: The block where the connection ends.

        Returns:
            True if there is a connection, False otherwise.
        """
        return (start_block, end_block) in self.connections
    

class WorkArea(QGraphicsView):
    """
    A custom QListView subclass that allows dropping items.

    Inherits from QGraphicsView.
    """

    def __init__(self, parent=None):
        """
        Initializes the WorkArea.

        Args:
            parent: The parent widget (default: None).
        """
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.setSceneRect(0, 0, 800, 600)  # Définir la taille de la scène
        self.installEventFilter(self)  # Installer un filtre d'événement sur l'objet lui-même
        self.setMouseTracking(True)  # Activer le suivi de la souris même sans clic
        self.last_y = 0
        self.connection_manager = ConnectionManager()
        self.temp_connection_start = None  # Point de départ temporaire pour la connexion en cours
        self.temp_connection_end = None  # Point de fin temporaire pour la connexion en cours

    def dragEnterEvent(self, event):
        """
        Event handler for drag enter event.

        Accepts the proposed action if the event's mime data has text.
        """
        if event.mimeData().hasText():
            event.acceptProposedAction()

    def dragMoveEvent(self, event):  
        """
        Event handler for drag move event.

        Accepts the event.
        """
        event.accept()
    
    def dropEvent(self, event):
        """
        Event handler for drop event.

        Args:
            event: The drop event.
        """
        block_type = event.mimeData().text()

        
        point = event.position().toPoint()
        

    
        pos = self.mapToScene(point)
        

        x, y, width, height = pos.x(), pos.y(), 100, 100  # Define position and size
        

        work_area = self  # Pass a reference to the work area

        if block_type == "For":
            print("For")
            block = ForBlockItem(x, y, width, height, work_area)
            
            self.scene.addItem(block)  # Add the block to the scene
            
             # Ajouter les points de connexion de block à la scène
            for input_point in block.for_block.input_connection_points:
                self.scene.addItem(input_point)
                print("Input point")
                print(input_point)
                
            for output_point in block.for_block.output_connection_points:
                self.scene.addItem(output_point)
                print("Output point")
                print(output_point)

        # Add conditions for other block types here
        elif block_type == "While":
            block = WhileBlockItem(x, y, width, height, work_area)
            self.scene.addItem(block)
        elif block_type == "Walk":
            block = WalkBlockItem(x, y, width, height, work_area)
            self.scene.addItem(block)

        block.setPos(pos.x() - width / 2, pos.y() - height / 2)
        event.acceptProposedAction()
        self.scene.update()
        print("Drop event at", pos.x(), pos.y())
        print([item for item in self.scene.items()])


    def mouseDoubleClickEvent(self, event):
        """
        Event handler for mouse double click event.

        Removes the item at the clicked position from the scene.

        Args:
            event: The mouse double click event.
        """
        # Get the item at the clicked position
        item = self.itemAt(event.pos())
        if item:
            # If there is an item at the clicked position, remove it from the scene
            self.scene.removeItem(item)
            del item  # Optional: delete the item to free memory

    def wheelEvent(self, event):
        """
        Event handler for wheel event.

        Zooms in or out when the wheel is turned.

        Args:
            event: The wheel event.
        """
        factor = 1.15 if event.angleDelta().y() > 0 else 1 / 1.15
        self.scale(factor, factor)
    
    def mousePressEvent(self, event):
        print("Mouse press event on")
        # Récupérer la position de la souris dans la scène
        scene_pos = self.mapToScene(event.pos())

        # Convertir les coordonnées QPointF en coordonnées entières
        scene_pos_int = QPoint(int(scene_pos.x()), int(scene_pos.y()))

        # Récupérer les éléments de la scène à la position donnée
        items = self.items(scene_pos_int)
        print("Liste des éléments de la scène :")
        for item in items:
            print("Type d'élément :", type(item))
            print("Position :", item.pos())

        colliding_items = self.collidingItems()
        print("Liste des éléments en collision :")
        for item in colliding_items:
            print("Type d'élément :", type(item))
            print("Position :", item.pos())
        

        # Vérifier si le clic est sur un point de connexion
        for item in items:
            if isinstance(item, QGraphicsEllipseItem) and getattr(item, 'isConnectionPoint', True):
                print(f"Point de connexion cliqué : {item}")
                if self.temp_connection_start is None:
                    # Si c'est le premier point de connexion sélectionné, enregistrer le point de départ temporaire
                    self.temp_connection_start = item
                elif self.temp_connection_start != item:
                    # Si c'est le deuxième point de connexion sélectionné (différent du premier), enregistrer le point de fin temporaire
                    self.temp_connection_end = item

                    # Créer la connexion entre les deux blocs
                    self.create_connection(self.temp_connection_start, self.temp_connection_end)

                    # Réinitialiser les points de connexion temporaires
                    self.temp_connection_start = None
                    self.temp_connection_end = None
        else:
            super().mousePressEvent(event)


    def mouseReleaseEvent(self, event):
        print("Mouse release event")
        # Réinitialiser les points de connexion temporaires si aucun point de connexion final n'a été sélectionné
        self.temp_connection_start = None
        self.temp_connection_end = None

        super().mouseReleaseEvent(event)





    def create_connection(self, start_point, end_point):
        """
        Crée une connexion entre deux points de connexion.

        Args:
            start_point: Le point de connexion de départ.
            end_point: Le point de connexion de fin.
        """
        # Vous devrez ajuster cette méthode pour créer une ligne ou tout autre visuel pour représenter la connexion entre les blocs.
        # Assurez-vous d'ajouter cette ligne ou ce visuel à la scène pour qu'il soit affiché correctement.
        line = QGraphicsLineItem(start_point.pos().x(), start_point.pos().y(),
                                  end_point.pos().x(), end_point.pos().y())
        line.setPen(QPen(Qt.GlobalColor.blue, 2))
        # Ajouter la connexion au gestionnaire de connexion
        self.connection_manager.add_connection(start_point.parent_block, end_point.parent_block)
    

    




class MainWindow(QMainWindow):
    """
    The main window of the application.
    """
    def on_off_clicked(self):
        print("Le bouton 'On/Off' a été cliqué!")

    def up_clicked(self):
        print("Le bouton 'Up' a été cliqué!")

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

    def __init__(self, parent=None):
        """
        Initializes the MainWindow.

        Args:
            parent: The parent widget (default: None).
        """
        super().__init__(parent)
        self.setWindowTitle("Get Jinxed !")
        self.setGeometry(100, 100, 800, 600)

        self.work_area = WorkArea(self)
        self.block_list = BlockList(self)

        block_names = ["Connection","For", "While","If","Else","Elif", "Walk", "Dance", "Rotate", "Side Step", "Scan", "Eye Move", "Stop", "Wait"]

        for i in range(len(block_names)):
            item = QListWidgetItem(block_names[i])
            self.block_list.addItem(item)


        button_names = ["On/Off", "Up", "Down", "Left", "Right", "Turn Left", "Turn Right"]

        button_layout = QVBoxLayout()

        for i in range(len(button_names)):
            button = QPushButton(button_names[i])
            button_layout.addWidget(button)
            
            if button_names[i] == "On/Off":
                button.clicked.connect(self.on_off_clicked)
            elif button_names[i] == "Up":
                button.clicked.connect(self.up_clicked)
            elif button_names[i] == "Down":
                button.clicked.connect(self.down_clicked)
            elif button_names[i] == "Left":
                button.clicked.connect(self.left_clicked)
            elif button_names[i] == "Right":
                button.clicked.connect(self.right_clicked)
            elif button_names[i] == "Turn Left":
                button.clicked.connect(self.turn_left_clicked)
            elif button_names[i] == "Turn Right":
                button.clicked.connect(self.turn_right_clicked)
        
         # Create a QGraphicsView
        self.view = QGraphicsView()

        # Set the scene of the QGraphicsView to the scene
        self.scene = QGraphicsScene()
        self.view.setScene(self.scene)

        # Now you can add the QGraphicsView to your main widget
        self.setCentralWidget(self.view)

        # Create blocks and add them to the scene
        self.for_block = ForBlockItem(0, 0, 100, 100, None)
        self.scene.addItem(self.for_block)

        self.while_block = WhileBlockItem(200, 0, 100, 100, None)
        self.scene.addItem(self.while_block)
            
        

        main_layout = QGridLayout()  # Main layout
        main_layout.addWidget(self.block_list, 0, 0)  # Add the block list to the left
        main_layout.addWidget(self.work_area, 0, 1)  # Add the work area in the middle
        main_layout.addLayout(button_layout, 0, 2)  # Add the buttons to the right

        central_widget = QWidget()  # Create a central widget
        central_widget.setLayout(main_layout)  # Set the main layout on the central widget
        self.setCentralWidget(central_widget)  # Set the central widget on the window
        self.setWindowIcon(QIcon('hehehe'))  

    def widgets(self):
        return self.findChildren(QWidget)
        
    

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()