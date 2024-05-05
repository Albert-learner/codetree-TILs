N = int(input())
lines = [tuple(map(int, input().split())) for _ in range(N)]
lines.sort(key = lambda x: abs(x[0] - x[1]))

lines = lines[:-1]
min_x1, max_x1 = min(list(zip(*lines))[0]), max(list(zip(*lines))[0])
min_x2, max_x2 = min(list(zip(*lines))[1]), max(list(zip(*lines))[1])

min_start, max_end = min(min_x1, min_x2), max(max_x1, max_x2)
print(abs(max_end - min_start))