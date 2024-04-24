N = int(input())
turnovers = [list(map(int, input().split())) for _ in range(N)]

max_cnts = 0
for stone in range(1, 4):
    maps = [0] * 4
    cnts = 0
    maps[stone] = 1
    for j in range(N):
        turnovers[j][0], turnovers[j][1] = turnovers[j][1], turnovers[j][0]
        maps[turnovers[j][0]], maps[turnovers[j][1]] = maps[turnovers[j][1]], maps[turnovers[j][0]]
        if maps[turnovers[j][2]] == 1:
            cnts += 1

    max_cnts = max(max_cnts, cnts)

print(max_cnts)