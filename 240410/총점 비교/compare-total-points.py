N = int(input())

class student:
    def __init__(self, name, first, second, third):
        self.name = name
        self.first = first
        self.second = second
        self.third = third

students = []
for _ in range(N):
    name, first, second, third = input().split()
    first, second, third = int(first), int(second), int(third)
    students.append(student(name, first, second, third))

students.sort(key = lambda x: x.first + x.second + x.third)
for student in students:
    print(student.name, student.first, student.second, student.third)