first = [list(map(int, input().split())) for _ in range(3)]
vacancy_line = input()
second = [list(map(int, input().split())) for _ in range(3)]

mul_matrix = [[0] * 3 for _ in range(3)]
for i in range(3):
    for j in range(3):
        mul_matrix[i][j] = first[i][j] * second[i][j]

for row in mul_matrix:
    print(*row)