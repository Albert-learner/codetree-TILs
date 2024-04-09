class PERSON:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight


people = []
for _ in range(5):
    name, height, weight = input().split()
    height, weight = int(height), float(weight)
    people.append(PERSON(name, height, weight))

name_sort = sorted(people, key = lambda x: x.name)
print("name")
for person in name_sort:
    print(person.name, person.height, person.weight)

print()
print("height")
height_sort = sorted(people, key = lambda x: -x.height)
for person in height_sort:
    print(person.name, person.height, person.weight)