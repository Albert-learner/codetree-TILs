code, color, second = input().split()
second = int(second)

class CODE:
    def __init__(self, code, color, second):
        self.code = code
        self.color = color
        self.second = second

    def print_code(self):
        print("code :", self.code)
        print("color :", self.color)
        print("second :", self.second)

code_inst = CODE(code, color, second)
code_inst.print_code()