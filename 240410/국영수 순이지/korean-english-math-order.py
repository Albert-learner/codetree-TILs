N = int(input())

class STUDENT:
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

students = []
for _ in range(N):
    name, kor, eng, math = input().split()
    kor, eng, math = int(kor), int(eng), int(math)
    students.append(STUDENT(name, kor, eng, math))

students.sort(key = lambda x: (x.kor, x.eng, x.math), reverse = True)
for student in students:
    print(student.name, student.kor, student.eng, student.math)