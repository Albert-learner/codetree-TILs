N = int(input())
points = [list(map(int, input().split())) + [num] for num in range(1, N + 1)]

points.sort(key = lambda x: int(abs(x[0])) + int(abs(x[1])))

for x, y, num in points:
    print(num)