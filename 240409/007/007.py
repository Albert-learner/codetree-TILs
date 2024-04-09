code, place, time = input().split()

class INFO:
    def __init__(self, code, place, time):
        self.code = code
        self.place = place
        self.time = int(time)

    def print_info(self):
        print("secret code :", self.code)
        print("meeting point :", self.place)
        print("time :", self.time)

info = INFO(code, place, time)
info.print_info()