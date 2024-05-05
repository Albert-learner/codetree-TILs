import sys

N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]

min_line = sys.maxsize
for i in range(N):
    excludeds = sorted(lines[:i] + lines[i + 1:])
    start, end = min(list(zip(*excludeds))[0]), max(list(zip(*excludeds))[1])
    min_line = min(min_line, end - start)

print(min_line)