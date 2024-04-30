N = int(input())
birds = sorted([tuple(map(int, input().split())) for _ in range(N)], key = lambda x: x[0])

cnts = 0
cur_bird = birds[0]
for i in range(1, N):
    if birds[i][0] != cur_bird[0]:
        cur_bird = birds[i]
    else:
        if birds[i][1] != cur_bird[1]:
            cur_bird = birds[i]
            cnts += 1

print(cnts)