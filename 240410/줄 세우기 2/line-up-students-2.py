N = int(input())
students = [list(map(int, input().split())) + [num] for num in range(1, N + 1)]

students.sort(key = lambda x: (x[0], -x[1]))

for h, w, num in students:
    print(h, w, num)