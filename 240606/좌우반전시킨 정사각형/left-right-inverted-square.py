N = int(input())

square = [[i * j for j in range(1, N + 1)] for i in range(1, N + 1)]

for row in square:
    print(*row[::-1])