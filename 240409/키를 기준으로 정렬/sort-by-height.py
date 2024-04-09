N = int(input())

class PERSON:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def print_person(self):
        print(self.name, self.height, self.weight)

people = []
for _ in range(N):
    name, height, weight = input().split()
    height, weight = int(height), int(weight)
    people.append(PERSON(name, height, weight))

people.sort(key = lambda x: x.height)

for person in people:
    person.print_person()