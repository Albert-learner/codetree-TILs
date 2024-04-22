K, N = map(int, input().split())
games = []

MAX_K, MAX_N = 10, 20
win_cnts = [[0] * (MAX_N + 1) for _ in range(MAX_N + 1)]

answer = 0
for _ in range(K):
    game = list(map(int, input().split()))
    games.append(game)

    for i in range(N):
        for j in range(i + 1, N):
            win_cnts[game[i]][game[j]] += 1

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if win_cnts[i][j] == K:
            answer += 1

print(answer)