class ForBlock:
    def __init__(self,var,range_start,range_end,body_block):
        self.var = var
        self.range_start = range_start
        self.range_end = range_end
        self.body_block = body_block
    
    def to_python_code(self):
        body_code=""
        for block in self.body_block:
            body_code += "    " + block.to_python_code() 
        return f"for {self.var} in range({self.range_start},{self.range_end}):\n{body_code}"

class WhileBlock:
    def __init__(self,condition,body_block):
        self.condition = condition
        self.body_block = body_block

    def to_python_code(self):
        body_code=""
        for block in self.body_block:
            body_code+="    "+block.to_python_code()
        return f"while {self.condition}:\n{body_code}"

class WalkBlock:
    def __init__(self,distance):
        self.distance = distance

    def to_python_code(self):
        return f"walk({self.distance})\n"

class DanceBlock:
    def __init__(self,dance_name):
        self.dance_name = dance_name

    def to_python_code(self):
        return f"dance({self.dance_name})\n"

class RotateBlock:
    def __init__(self,angle):
        self.angle = angle

    def to_python_code(self):
        return f"rotate({self.angle})\n"
    
class SideStepBlock:
    def __init__(self,distance):
        self.distance = distance

    def to_python_code(self):
        return f"side_step({self.distance})\n"
    
class ScanBlock:
    def __init__(self):
        pass

    def to_python_code(self):
        return "scan()\n"

class EyeMoveBlock:
    def __init__(self,direction):
        self.direction = direction

    def to_python_code(self):
        return f"eye_move({self.direction})\n"

class StopBlock:
    def __init__(self):
        pass

    def to_python_code(self):
        return "stop()\n"
    

        

#blocks = get_blocks_from_ui()
blocks = [
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
for block in blocks:
    code += block.to_python_code()

# Exécutez le code


print(code)