from PyQt6.QtWidgets import QApplication, QMainWindow,QGridLayout, QPushButton, QVBoxLayout, QWidget, QListWidget, QListWidgetItem, QGraphicsTextItem, QGraphicsScene, QGraphicsView, QGraphicsItem,QGraphicsRectItem,QGraphicsWidget, QGraphicsProxyWidget
from PyQt6.QtCore import Qt, QMimeData, QRectF
from PyQt6.QtGui import QDrag, QCursor, QIcon

from design import BlockBase
from design import ForBlockWidget
from design import WhileBlockWidget
from design import WalkBlockWidget

#Création class Block
class Block(QGraphicsWidget, BlockBase):
    def __init__(self, x, y, width, height, work_area):
        QGraphicsWidget.__init__(self)
        BlockBase.__init__(self)
        self.setGeometry(x, y, width, height)
        self.work_area = work_area

class ForBlockItem(QGraphicsProxyWidget):
    def __init__(self, x, y, width, height, work_area):
        super().__init__()
        self.setGeometry(QRectF(x, y, width, height))
        print(x, y, width, height)
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
            print(x, y)
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
        self.last_y = 0

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
        print(point)

    
        pos = self.mapToScene(point)
        print(pos)

        x, y, width, height = pos.x(), pos.y(), 100, 100  # Define position and size
        print(x, y, width, height)

        work_area = self  # Pass a reference to the work area

        if block_type == "For":
            block = ForBlockItem(x, y, width, height, work_area)
            
            self.scene.addItem(block)  # Add the block to the scene
            print(x, y, width, height)

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

    

    def mouseReleaseEvent(self, event):
        """
        Event handler for mouse release event.

        Stops panning when the middle mouse button is released.

        Args:
            event: The mouse release event.
        """
        if event.button() == Qt.MouseButton.RightButton:
            self.setDragMode(QGraphicsView.DragMode.NoDrag)
        super().mouseReleaseEvent(event)



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
        
    

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()