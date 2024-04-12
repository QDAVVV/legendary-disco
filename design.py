from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton

class BlockBase(QWidget):
    """
    A custom QWidget subclass that serves as the base class for all blocks.
    """
    class BlockBase(QWidget):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            layout = QVBoxLayout()
            label = QLabel("Block")
            layout.addWidget(label)
            self.setLayout(layout)


from PyQt6.QtWidgets import QGraphicsWidget, QGraphicsRectItem, QGraphicsLinearLayout, QGraphicsProxyWidget, QLineEdit, QPushButton, QGraphicsItem
from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import QGraphicsWidget, QGraphicsRectItem, QGraphicsLinearLayout, QLineEdit, QPushButton, QGraphicsItem

from PyQt6.QtWidgets import QGraphicsWidget, QGraphicsRectItem, QGraphicsLinearLayout, QLineEdit, QPushButton, QGraphicsProxyWidget, QGraphicsItem

from PyQt6.QtWidgets import QGraphicsWidget, QGraphicsRectItem, QGraphicsLinearLayout, QLineEdit, QPushButton, QGraphicsItem

class ForBlockWidget(QGraphicsWidget):
    def __init__(self):
        super().__init__()

        # Create a rectangle item to represent the visual appearance of the block
        self.rect_item = QGraphicsRectItem(0, 0, 200, 100, self)
        self.rect_item.setBrush(Qt.GlobalColor.blue)  # Set the color of the block
        self.rect_item.setPen(Qt.GlobalColor.black)  # Set the border color

        # Create a layout for organizing the internal widgets
        self.layout = QGraphicsLinearLayout(Qt.Orientation.Vertical)
        self.setLayout(self.layout)

        # Add widgets for editing parameters
        self.variable_edit = QLineEdit("i")
        self.range_start_edit = QLineEdit("0")
        self.range_end_edit = QLineEdit("10")

        variable_edit_proxy = QGraphicsProxyWidget()
        variable_edit_proxy.setWidget(self.variable_edit)

        range_start_edit_proxy = QGraphicsProxyWidget()
        range_start_edit_proxy.setWidget(self.range_start_edit)

        range_end_edit_proxy = QGraphicsProxyWidget()
        range_end_edit_proxy.setWidget(self.range_end_edit)


        self.layout.addItem(variable_edit_proxy)
        self.layout.addItem(range_start_edit_proxy)
        self.layout.addItem(range_end_edit_proxy)

        # Add buttons for connecting to other blocks
        self.input_button = QPushButton("Input")
        self.output_loop_button = QPushButton("Loop Output")
        self.output_after_button = QPushButton("After Loop Output")

        input_button_proxy = QGraphicsProxyWidget()
        input_button_proxy.setWidget(self.input_button)

        output_loop_button_proxy = QGraphicsProxyWidget()
        output_loop_button_proxy.setWidget(self.output_loop_button)

        output_after_button_proxy = QGraphicsProxyWidget()
        output_after_button_proxy.setWidget(self.output_after_button)

        self.layout.addItem(input_button_proxy)
        self.layout.addItem(output_loop_button_proxy)
        self.layout.addItem(output_after_button_proxy)

        # Set the position and size of the block
        self.setPos(0, 0)
        self.rect_item.setRect(0, 0, self.boundingRect().width(), self.boundingRect().height())

        # Add the rectangle item to the widget
        

