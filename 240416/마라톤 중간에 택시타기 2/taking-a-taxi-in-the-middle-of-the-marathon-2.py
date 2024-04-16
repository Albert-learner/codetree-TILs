N = int(input())
chkpnts = [list(map(int, input().split())) for _ in range(N)]

def distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)

total = 0
for i in range(N - 1):
    total += distance(chkpnts[i][0], chkpnts[i][1], chkpnts[i + 1][0], chkpnts[i + 1][1])

answer = float("inf")
for i in range(1, N - 1):
    check = total - distance(chkpnts[i - 1][0], chkpnts[i - 1][1], chkpnts[i][0], chkpnts[i][1])\
                  - distance(chkpnts[i][0], chkpnts[i][1], chkpnts[i + 1][0], chkpnts[i + 1][1])\
                  + distance(chkpnts[i - 1][0], chkpnts[i - 1][1], chkpnts[i + 1][0], chkpnts[i + 1][1])

    answer = min(answer, check)

print(answer)