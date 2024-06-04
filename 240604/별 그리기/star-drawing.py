N = int(input())

size = 2 * N - 1
for i in range(size):
    distance = abs(N - 1 - i)
    line = ' ' * distance
    line += '*' * (size - 2 * distance)
    print(line)