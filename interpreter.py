from UI import UI
class ForBlock:
    def __init__(self, var, range_start, range_end, body_block):
        self.var = var
        self.range_start = range_start
        self.range_end = range_end
        self.body_block = body_block
        self.inputs = None  # Liste pour stocker les blocs connectés en entrée
        self.output = None  # Bloc connecté en sortie
    
    def add_input(self, block):
        self.inputs = block
    
    def set_output(self, block):
        self.output = block
    
    def to_python_code(self):
        body_code = ""
        for block in self.body_block:
            body_code += "    " + block.to_python_code()
        return f"for {self.var} in range({self.range_start}, {self.range_end}):\n{body_code}"


class WhileBlock:
    def __init__(self,condition,body_block):
        self.condition = condition
        self.body_block = body_block
        self.inputs = None  # Liste pour stocker les blocs connectés en entrée
        self.output = None  # Bloc connecté en sortie
    
    def add_input(self, block):
        self.inputs=block
    
    def set_output(self, block):
        self.output = block

    def to_python_code(self):
        body_code=""
        for block in self.body_block:
            body_code+="    "+block.to_python_code()
        return f"while {self.condition}:\n{body_code}"

class WalkBlock:
    def __init__(self,distance):
        self.distance = distance
        self.inputs = None  # Liste pour stocker les blocs connectés en entrée
        self.output = None  # Bloc connecté en sortie
    
    def add_input(self, block):
        self.input = block
    
    def set_output(self, block):
        self.output = block

    def to_python_code(self):
        return f"walk({self.distance})\n"

class DanceBlock:
    def __init__(self,dance_name):
        self.dance_name = dance_name
        self.inputs = None  # Liste pour stocker les blocs connectés en entrée
        self.output = None  # Bloc connecté en sortie
    
    def add_input(self, block):
        self.input = block
    
    def set_output(self, block):
        self.output = block

    def to_python_code(self):
        return f"dance({self.dance_name})\n"

class RotateBlock:
    def __init__(self,angle):
        self.angle = angle
        self.inputs = None  # Liste pour stocker les blocs connectés en entrée
        self.output = None  # Bloc connecté en sortie
    
    def add_input(self, block):
        self.input = block
    
    def set_output(self, block):
        self.output = block

    def to_python_code(self):
        return f"rotate({self.angle})\n"
    
class SideStepBlock:
    def __init__(self,distance):
        self.distance = distance
        self.inputs = None  # Liste pour stocker les blocs connectés en entrée
        self.output = None  # Bloc connecté en sortie
    
    def add_input(self, block):
        self.input = block
    
    def set_output(self, block):
        self.output = block

    def to_python_code(self):
        return f"side_step({self.distance})\n"
    
class ScanBlock:
    def __init__(self):
        pass
        self.inputs = None  # Liste pour stocker les blocs connectés en entrée
        self.output = None  # Bloc connecté en sortie
    
    def add_input(self, block):
        self.input = block
    
    def set_output(self, block):
        self.output = block

    def to_python_code(self):
        return "scan()\n"

class EyeMoveBlock:
    def __init__(self,direction):
        self.direction = direction
        self.inputs = None  # Liste pour stocker les blocs connectés en entrée
        self.output = None  # Bloc connecté en sortie
    
    def add_input(self, block):
        self.input = block
    
    def set_output(self, block):
        self.output = block

    def to_python_code(self):
        return f"eye_move({self.direction})\n"

class StopBlock:
    def __init__(self):
        pass
        self.inputs = None  # Liste pour stocker les blocs connectés en entrée
        self.output = None  # Bloc connecté en sortie
    
    def add_input(self, block):
        self.input = block
    
    def set_output(self, block):
        self.output = block

    def to_python_code(self):
        return "stop()\n"
    
class IfBlock:
    def __init__(self,condition,body_block):
        self.condition = condition
        self.body_block = body_block
        self.inputs = None  # Liste pour stocker les blocs connectés en entrée
        self.output = None  # Bloc connecté en sortie
    
    def add_input(self, block):
        self.input = block
    
    def set_output(self, block):
        self.output = block

    def to_python_code(self):
        body_code=""
        for block in self.body_block:
            body_code+="    "+block.to_python_code()
        return f"if {self.condition}:\n{body_code}"

class ElseBlock:
    def __init__(self,body_block):
        self.body_block = body_block
        self.inputs = None  # Liste pour stocker les blocs connectés en entrée
        self.output = None  # Bloc connecté en sortie
    
    def add_input(self, block):
        self.input = block
    
    def set_output(self, block):
        self.output = block

    def to_python_code(self):
        body_code=""
        for block in self.body_block:
            body_code+="    "+block.to_python_code()
        return f"else:\n{body_code}"

class ElifBlock:
    def __init__(self,condition,body_block):
        self.condition = condition
        self.body_block = body_block
        self.inputs = None  # Liste pour stocker les blocs connectés en entrée
        self.output = None  # Bloc connecté en sortie
    
    def add_input(self, block):
        self.input = block
    
    def set_output(self, block):
        self.output = block

    def to_python_code(self):
        body_code=""
        for block in self.body_block:
            body_code+="    "+block.to_python_code()
        return f"elif {self.condition}:\n{body_code}"
    
class ConnectBlock:
    def __init__(self,robot_name):
        self.robot_name = robot_name
        self.inputs = None  # Liste pour stocker les blocs connectés en entrée
        self.output = None  # Bloc connecté en sortie
    
    def add_input(self, block):
        self.input = block
    
    def set_output(self, block):
        self.output = block

    def to_python_code(self):
        return f"connect({self.robot_name})\n"

        

def get_blocks_from_ui():
    blocks = []
    for widget in UI.widgets():
        if isinstance(widget, ForBlock):
            blocks.append(ForBlock(widget.variable_edit.text(), widget.range_start_edit.text(), widget.range_end_edit.text(), get_blocks_from_ui(widget)))
        if isinstance(widget, WhileBlock):
            blocks.append(WhileBlock(widget.condition_edit.text(), get_blocks_from_ui(widget)))
        if isinstance(widget, WalkBlock):
            blocks.append(WalkBlock(widget.steps_edit.text()))
        if isinstance(widget, DanceBlock):
            blocks.append(DanceBlock(widget.dance_edit.text()))
        if isinstance(widget, RotateBlock):
            blocks.append(RotateBlock(widget.angle_edit.text()))
        if isinstance(widget, SideStepBlock):
            blocks.append(SideStepBlock(widget.steps_edit.text()))
        if isinstance(widget, ScanBlock):
            blocks.append(ScanBlock())
        
    return blocks
        

blockss = [
    ForBlock("i",0,10,[WalkBlock(10),RotateBlock(90)]),
    WhileBlock("True",[WalkBlock(10),RotateBlock(90)]),
    WalkBlock(10),
    DanceBlock("tango"),
    RotateBlock(90),
    SideStepBlock(10),
    ScanBlock(),
    EyeMoveBlock("left"),
    StopBlock()
]
code = ""
for block in blockss:
    code += block.to_python_code()

# Exécutez le code
try:
    exec(code)
except Exception as e:
    print(f"Error: {e}")

print(code)