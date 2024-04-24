from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton,QGraphicsWidget, QGraphicsProxyWidget, QGraphicsLinearLayout
from PyQt6.QtGui import QPainter, QColor, QPen
from PyQt6.QtCore import Qt, QRectF
from PyQt6.QtWidgets import QGraphicsEllipseItem

class ConnectionPoint(QGraphicsEllipseItem):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptHoverEvents(True)
        self.isConnectionPoint = True
        self.default_color = Qt.GlobalColor.black
        self.hover_color = Qt.GlobalColor.green
        self.clicked_color = Qt.GlobalColor.red
        self.setBrush(self.default_color)
        # Activer la réception des événements de survol
        self.setAcceptHoverEvents(True)

    def hoverEnterEvent(self, event):
        self.setBrush(self.hover_color)
        super().hoverEnterEvent(event)

    def hoverLeaveEvent(self, event):
        self.setBrush(self.default_color)
        super().hoverLeaveEvent(event)

    def mousePressEvent(self, event):
        self.setBrush(self.clicked_color)
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.setBrush(self.default_color)
        super().mouseReleaseEvent(event)


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
        range_start_edit = QLineEdit("0")
        range_end_edit = QLineEdit("10")

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

        self.input_connection_points = []
        self.output_connection_points = []

        

    def add_input_connection_points(self):
        width = self.size().width()
        height = self.size().height()

        input_point1 = ConnectionPoint(self)
        input_point1.setPos(width * 0.9, height * 0.25)
        input_point1.setRect(-5, -5, 10, 10)

        input_point2 = ConnectionPoint(self)
        input_point2.setPos(width * 0.9, height * 0.75)
        input_point2.setRect(-5, -5, 10, 10)

        # Add input points to the scene
        scene = self.scene()
        if scene:
            scene.addItem(input_point1)
            scene.addItem(input_point2)


        self.input_connection_points.extend([input_point1, input_point2])

    def add_output_connection_points(self):
        width = self.size().width()
        print(width)
        height = self.size().height()
        print(height)

        output_point = ConnectionPoint(self)
        output_point.setPos(width * 0.1, height * 0.5)
        output_point.setRect(-5, -5, 10, 10)

        scene = self.scene()
        if scene:
            scene.addItem(output_point)


        self.output_connection_points.append(output_point)

    def paint(self, painter, option, widget):
        
        """
        Override the paint method to draw connection points.
        """
        if not self.input_connection_points:
            self.add_input_connection_points()
        if not self.output_connection_points:
            self.add_output_connection_points()
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        # Call the base class paint method to draw the layout
        super().paint(painter, option, widget)

        # Draw ellipses for input connection points
        painter.setBrush(Qt.GlobalColor.black)
        for ellipse in self.input_connection_points:
            painter.drawEllipse(ellipse.rect())

        # Draw ellipse for output connection point
        painter.setBrush(Qt.GlobalColor.red)
        painter.drawEllipse(self.output_connection_points[0].rect())

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