N = int(input())

class person:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

people = []
for _ in range(N):
    name, height, weight = input().split()
    height, weight = int(height), int(weight)
    people.append(person(name, height, weight))

people.sort(key = lambda x: (x.height, -x.weight))

for person in people:
    print(person.name, person.height, person.weight)