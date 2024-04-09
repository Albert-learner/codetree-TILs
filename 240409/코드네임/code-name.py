class Members:
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.mem_lst = []
        self.mem_lst.append([name, score])
        self.mem_lst.sort(key = lambda x: x[1])

    def print_min_member(self):
        print(*self.mem_lst[0])

members = []
for _ in range(5):
    name, score = input().split()
    score = int(score)
    members.append(Members(name, score))

members[0].print_min_member()