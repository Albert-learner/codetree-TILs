N = int(input())

class PERSON:
    def __init__(self, name, road, province):
        self.name = name
        self.road = road
        self.province = province

    def print_info(self):
        print("name", self.name)
        print("addr", self.road)
        print("city", self.province)

people = []
for _ in range(N):
    name, road, province = input().split()
    people.append(PERSON(name, road, province))

fast_member = sorted(people, key = lambda x: x.name, reverse = True)[0]
fast_member.print_info()