N = int(input())
turnovers = [list(map(int, input().split())) for _ in range(N)]

max_cnts = 0
for stone in range(1, 4):
    maps = [0] * 4
    cnts = 0
    maps[stone] = 1
    for a, b, c in turnovers:
        maps[a], maps[b] = maps[b], maps[a]
        if maps[c]:
            cnts += 1

    max_cnts = max(max_cnts, cnts)

print(max_cnts)