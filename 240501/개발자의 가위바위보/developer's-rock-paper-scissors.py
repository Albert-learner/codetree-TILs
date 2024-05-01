N = int(input())
games = [list(map(int, input().split())) for _ in range(N)]

wins, max_wins = 0, 0
for a, b in games:
    if a == 1 and b == 2:
        wins += 1
    elif a == 1 and b == 3:
        wins += 1
    elif a == 3 and b == 1:
        wins += 1

max_wins = max(max_wins, wins)
wins = 0
for a, b in games:
    if a == 1 and b == 3:
        wins += 1
    elif a == 3 and b == 2:
        wins += 1
    elif a == 2 and b == 1:
        wins += 1

max_wins = max(max_wins, wins)
print(max_wins)