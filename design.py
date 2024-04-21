from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton,QGraphicsWidget, QGraphicsProxyWidget, QGraphicsLinearLayout
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6.QtCore import Qt, QRectF

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

class ForBlockWidget(QGraphicsWidget):
    def __init__(self):
        super().__init__()

        # Create a layout for organizing the internal widgets
        layout = QGraphicsLinearLayout(Qt.Orientation.Vertical)
        self.setLayout(layout)

        # Add widgets for editing parameters
        variable_edit = QLineEdit("i")
        variable_edit.setFixedWidth(20)
        range_start_edit = QLineEdit("0")
        range_start_edit.setFixedWidth(20)
        range_end_edit = QLineEdit("10")
        range_end_edit.setFixedWidth(20)    

        variable_edit_proxy = QGraphicsProxyWidget()
        variable_edit_proxy.setWidget(variable_edit)

        range_start_edit_proxy = QGraphicsProxyWidget()
        range_start_edit_proxy.setWidget(range_start_edit)

        range_end_edit_proxy = QGraphicsProxyWidget()
        range_end_edit_proxy.setWidget(range_end_edit)

        layout.addItem(variable_edit_proxy)
        layout.addItem(range_start_edit_proxy)
        layout.addItem(range_end_edit_proxy)

        # Set the minimum size of the block
        layout.setMinimumSize(200, 100)

    def paint(self, painter, option, widget):
        """
        Override the paint method to draw connection points.
        """
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Get widget dimensions
        width = self.size().width()
        height = self.size().height()

        # Draw input connection points
        painter.setBrush(Qt.GlobalColor.black)
        painter.drawEllipse(int(width - 10), int(height / 4), 10, 10)
        painter.drawEllipse(int(width - 10), int(height * 3 / 4), 10, 10)

        # Draw output connection points
        painter.setBrush(Qt.GlobalColor.red)
        painter.drawEllipse(0, int(height / 2 - 5), 10, 10)

class WhileBlockWidget(QGraphicsWidget):
    def __init__(self):
        super().__init__()

        # Create a layout for organizing the internal widgets
        layout = QGraphicsLinearLayout(Qt.Orientation.Vertical)
        self.setLayout(layout)

        # Add widgets for editing parameters
        condition_edit = QLineEdit("i < 10")

        condition_edit_proxy = QGraphicsProxyWidget()
        condition_edit_proxy.setWidget(condition_edit)

        layout.addItem(condition_edit_proxy)

        # Set the minimum size of the block
        layout.setMinimumSize(200, 100)

    def paint(self, painter, option, widget):
        """
        Override the paint method to draw connection points.
        """
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Get widget dimensions
        width = self.size().width()
        height = self.size().height()

        # Draw input connection points
        painter.setBrush(Qt.GlobalColor.black)
        painter.drawEllipse(int(width - 10), int(height / 4), 10, 10)
        painter.drawEllipse(int(width - 10), int(height * 3 / 4), 10, 10)

        # Draw output connection points
        painter.setBrush(Qt.GlobalColor.red)
        painter.drawEllipse(0, int(height / 2 - 5), 10, 10)

class WalkBlockWidget(QGraphicsWidget):
    def __init__(self):
        super().__init__()

        # Create a layout for organizing the internal widgets
        layout = QGraphicsLinearLayout(Qt.Orientation.Vertical)
        self.setLayout(layout)

        # Add widgets for editing parameters
        steps_edit = QLineEdit("10")

        steps_edit_proxy = QGraphicsProxyWidget()
        steps_edit_proxy.setWidget(steps_edit)

        layout.addItem(steps_edit_proxy)

        # Set the minimum size of the block
        layout.setMinimumSize(200, 100)

    def paint(self, painter, option, widget):
        """
        Override the paint method to draw connection points.
        """
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Get widget dimensions
        width = self.size().width()
        height = self.size().height()

        # Draw input connection points
        painter.setBrush(Qt.GlobalColor.black)
        painter.drawEllipse(int(width - 10), int(height / 2 - 5), 10, 10)

        # Draw output connection points
        painter.setBrush(Qt.GlobalColor.red)
        painter.drawEllipse(0, int(height / 2 - 5), 10, 10)


class SideStepBlockWidget(QGraphicsWidget):
    def __init__(self):
        super().__init__()

        # Create a layout for organizing the internal widgets
        layout = QGraphicsLinearLayout(Qt.Orientation.Vertical)
        self.setLayout(layout)

        # Add widgets for editing parameters
        steps_edit = QLineEdit("10")

        steps_edit_proxy = QGraphicsProxyWidget()
        steps_edit_proxy.setWidget(steps_edit)

        layout.addItem(steps_edit_proxy)

        # Set the minimum size of the block
        layout.setMinimumSize(200, 100)

    def paint(self, painter, option, widget):
        """
        Override the paint method to draw connection points.
        """
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Get widget dimensions
        width = self.size().width()
        height = self.size().height()

        # Draw input connection points
        painter.setBrush(Qt.GlobalColor.black)
        painter.drawEllipse(int(width - 10), int(height / 2 - 5), 10, 10)

        # Draw output connection points
        painter.setBrush(Qt.GlobalColor.red)
        painter.drawEllipse(0, int(height / 2 - 5), 10, 10)

class ScanBlockWidget(QGraphicsWidget):
    def __init__(self):
        super().__init__()

        # Create a layout for organizing the internal widgets
        layout = QGraphicsLinearLayout(Qt.Orientation.Vertical)
        self.setLayout(layout)

        # Add widgets for editing parameters
        steps_edit = QLineEdit("10")

        steps_edit_proxy = QGraphicsProxyWidget()
        steps_edit_proxy.setWidget(steps_edit)

        layout.addItem(steps_edit_proxy)

        # Set the minimum size of the block
        layout.setMinimumSize(200, 100)

    def paint(self, painter, option, widget):
        """
        Override the paint method to draw connection points.
        """
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Get widget dimensions
        width = self.size().width()
        height = self.size().height()

        # Draw input connection points
        painter.setBrush(Qt.GlobalColor.black)
        painter.drawEllipse(int(width - 10), int(height / 2 - 5), 10, 10)

        # Draw output connection points
        painter.setBrush(Qt.GlobalColor.red)
        painter.drawEllipse(0, int(height / 2 - 5), 10, 10)

class EyeBlockWidget(QGraphicsWidget):
    def __init__(self):
        super().__init__()

        # Create a layout for organizing the internal widgets
        layout = QGraphicsLinearLayout(Qt.Orientation.Vertical)
        self.setLayout(layout)

        # Add widgets for editing parameters
        steps_edit = QLineEdit("10")

        steps_edit_proxy = QGraphicsProxyWidget()
        steps_edit_proxy.setWidget(steps_edit)

        layout.addItem(steps_edit_proxy)

        # Set the minimum size of the block
        layout.setMinimumSize(200, 100)

    def paint(self, painter, option, widget):
        """
        Override the paint method to draw connection points.
        """
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Get widget dimensions
        width = self.size().width()
        height = self.size().height()

        # Draw input connection points
        painter.setBrush(Qt.GlobalColor.black)
        painter.drawEllipse(int(width - 10), int(height / 2 - 5), 10, 10)

        # Draw output connection points
        painter.setBrush(Qt.GlobalColor.red)
        painter.drawEllipse(0, int(height / 2 - 5), 10, 10)

class StopBlockWidget(QGraphicsWidget):
    def __init__(self):
        super().__init__()

        # Create a layout for organizing the internal widgets
        layout = QGraphicsLinearLayout(Qt.Orientation.Vertical)
        self.setLayout(layout)

        # Add widgets for editing parameters
        steps_edit = QLineEdit("10")

        steps_edit_proxy = QGraphicsProxyWidget()
        steps_edit_proxy.setWidget(steps_edit)

        layout.addItem(steps_edit_proxy)

        # Set the minimum size of the block
        layout.setMinimumSize(200, 100)

    def paint(self, painter, option, widget):
        """
        Override the paint method to draw connection points.
        """
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Get widget dimensions
        width = self.size().width()
        height = self.size().height()

        # Draw input connection points
        painter.setBrush(Qt.GlobalColor.black)
        painter.drawEllipse(int(width - 10), int(height / 2 - 5), 10, 10)

        # Draw output connection points
        painter.setBrush(Qt.GlobalColor.red)
        painter.drawEllipse(0, int(height / 2 - 5), 10, 10)

class WaitBlockWidget(QGraphicsWidget):
    def __init__(self):
        super().__init__()

        # Create a layout for organizing the internal widgets
        layout = QGraphicsLinearLayout(Qt.Orientation.Vertical)
        self.setLayout(layout)

        # Add widgets for editing parameters
        steps_edit = QLineEdit("10")

        steps_edit_proxy = QGraphicsProxyWidget()
        steps_edit_proxy.setWidget(steps_edit)

        layout.addItem(steps_edit_proxy)

        # Set the minimum size of the block
        layout.setMinimumSize(200, 100)

    def paint(self, painter, option, widget):
        """
        Override the paint method to draw connection points.
        """
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Get widget dimensions
        width = self.size().width()
        height = self.size().height()

        # Draw input connection points
        painter.setBrush(Qt.GlobalColor.black)
        painter.drawEllipse(int(width - 10), int(height / 2 - 5), 10, 10)

        # Draw output connection points
        painter.setBrush(Qt.GlobalColor.red)
        painter.drawEllipse(0, int(height / 2 - 5), 10, 10)

class ConnectBlockWidget(QGraphicsWidget):
    def __init__(self):
        super().__init__()

        # Create a layout for organizing the internal widgets
        layout = QGraphicsLinearLayout(Qt.Orientation.Vertical)
        self.setLayout(layout)

        # Add widgets for editing parameters
        steps_edit = QLineEdit("10")

        steps_edit_proxy = QGraphicsProxyWidget()
        steps_edit_proxy.setWidget(steps_edit)

        layout.addItem(steps_edit_proxy)

        # Set the minimum size of the block
        layout.setMinimumSize(200, 100)

    def paint(self, painter, option, widget):
        """
        Override the paint method to draw connection points.
        """
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Get widget dimensions
        width = self.size().width()
        height = self.size().height()

        # Draw input connection points
        painter.setBrush(Qt.GlobalColor.black)
        painter.drawEllipse(int(width - 10), int(height / 2 - 5), 10, 10)

        # Draw output connection points
        painter.setBrush(Qt.GlobalColor.red)
        painter.drawEllipse(0, int(height / 2 - 5), 10, 10)

class IfBlockWidget(QGraphicsWidget):
    def __init__(self):
        super().__init__()

        # Create a layout for organizing the internal widgets
        layout = QGraphicsLinearLayout(Qt.Orientation.Vertical)
        self.setLayout(layout)

        # Add widgets for editing parameters
        condition_edit = QLineEdit("i < 10")

        condition_edit_proxy = QGraphicsProxyWidget()
        condition_edit_proxy.setWidget(condition_edit)

        layout.addItem(condition_edit_proxy)

        # Set the minimum size of the block
        layout.setMinimumSize(200, 100)

    def paint(self, painter, option, widget):
        """
        Override the paint method to draw connection points.
        """
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Get widget dimensions
        width = self.size().width()
        height = self.size().height()

        # Draw input connection points
        painter.setBrush(Qt.GlobalColor.black)
        painter.drawEllipse(int(width - 10), int(height / 4), 10, 10)
        painter.drawEllipse(int(width - 10), int(height * 3 / 4), 10, 10)

        # Draw output connection points
        painter.setBrush(Qt.GlobalColor.red)
        painter.drawEllipse(0, int(height / 2 - 5), 10, 10)

class ElseBlockWidget(QGraphicsWidget):
    def __init__(self):
        super().__init__()

        # Create a layout for organizing the internal widgets
        layout = QGraphicsLinearLayout(Qt.Orientation.Vertical)
        self.setLayout(layout)

        # Add widgets for editing parameters
        steps_edit = QLineEdit("10")

        steps_edit_proxy = QGraphicsProxyWidget()
        steps_edit_proxy.setWidget(steps_edit)

        layout.addItem(steps_edit_proxy)

        # Set the minimum size of the block
        layout.setMinimumSize(200, 100)

    def paint(self, painter, option, widget):
        """
        Override the paint method to draw connection points.
        """
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Get widget dimensions
        width = self.size().width()
        height = self.size().height()

        # Draw input connection points
        painter.setBrush(Qt.GlobalColor.black)
        painter.drawEllipse(int(width - 10), int(height / 4), 10, 10)
        painter.drawEllipse(int(width - 10), int(height * 3 / 4), 10, 10)

        # Draw output connection points
        painter.setBrush(Qt.GlobalColor.red)
        painter.drawEllipse(0, int(height / 2 - 5), 10, 10) 

class ElifBlockWidget(QGraphicsWidget):
    def __init__(self):
        super().__init__()

        # Create a layout for organizing the internal widgets
        layout = QGraphicsLinearLayout(Qt.Orientation.Vertical)
        self.setLayout(layout)

        # Add widgets for editing parameters
        condition_edit = QLineEdit("i < 10")

        condition_edit_proxy = QGraphicsProxyWidget()
        condition_edit_proxy.setWidget(condition_edit)

        layout.addItem(condition_edit_proxy)

        # Set the minimum size of the block
        layout.setMinimumSize(200, 100)

    def paint(self, painter, option, widget):
        """
        Override the paint method to draw connection points.
        """
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Get widget dimensions
        width = self.size().width()
        height = self.size().height()

        # Draw input connection points
        painter.setBrush(Qt.GlobalColor.black)
        painter.drawEllipse(int(width - 10), int(height / 4), 10, 10)
        painter.drawEllipse(int(width - 10), int(height * 3 / 4), 10, 10)

        # Draw output connection points
        painter.setBrush(Qt.GlobalColor.red)
        painter.drawEllipse(0, int(height / 2 - 5), 10, 10)