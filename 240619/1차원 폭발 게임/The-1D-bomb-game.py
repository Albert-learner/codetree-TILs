N, M = map(int, input().split())
bombs = [int(input()) for _ in range(N)]

def get_consecutive_counts(bombs):
    n = len(bombs)
    consecutive_cnts = [0] * n
    cnts = 0
    for i in range(n - 1, 0, -1):
        if bombs[i] == bombs[i - 1]:
            cnts += 1
        else:
            cnts = 0
        consecutive_cnts[i] = cnts
    
    return consecutive_cnts

def can_bomb(consecutive_cnts, m):
    return any(cnts >= m - 1 for cnts in consecutive_cnts)

def explode(bombs, consecutive_cnts, m):
    if m == 1:
        return []

    n = len(bombs)
    bombed = [0] * n
    for i, cnts in enumerate(consecutive_cnts):
        if cnts >= m - 1:
            for j in range(i - 1, i + cnts):
                bombed[j] = 1

    return [bombs[i] for i in range(n) if not bombed[i]]

while True:
    consecutive_cnts = get_consecutive_counts(bombs)
    if not can_bomb(consecutive_cnts, M):
        break

    bombs = explode(bombs, consecutive_cnts, M)

print(len(bombs))
for bomb in bombs:
    print(bomb)