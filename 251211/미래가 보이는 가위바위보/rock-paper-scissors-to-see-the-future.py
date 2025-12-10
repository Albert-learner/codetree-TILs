N = int(input())
B = [input() for _ in range(N)]

# Please write your code here.
gests = ["H", "S", "P"]

def win(gest, opp):
    return (gest == 'H' and opp == 'S') or \
           (gest == 'S' and opp == 'P') or \
           (gest == 'P' and opp == 'H')

L = [[0] * 3 for _ in range(N + 1)]
for i in range(1, N + 1):
    opp = B[i - 1]
    for g in range(3):
        L[i][g] = L[i - 1][g] + (1 if win(gests[g], opp) else 0)

R = [[0] * 3 for _ in range(N + 1)]
for i in range(N - 1, -1, -1):
    opp = B[i]
    for g in range(3):
        R[i][g] = R[i + 1][g] + (1 if win(gests[g], opp) else 0)

ans = 0
for k in range(N + 1):
    bestL = max(L[k])
    bestR = max(R[k])
    ans = max(ans, bestL + bestR)

print(ans)