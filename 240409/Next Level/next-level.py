person_id, level = input().split()

class game_info:
    def __init__(self, person_id = "codetree", level = 10):
        self.person_id = person_id
        self.level = level

    def print_info(self):
        print("user " + self.person_id + " lv", self.level)

games = game_info()
games.print_info()
games = game_info(person_id, level)
games.print_info()