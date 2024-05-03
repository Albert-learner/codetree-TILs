from collections import deque

class Push:
    def __init__(self, row, col):
        self.r = row
        self.c = col

def index_ok(r, c):
    return 0 <= r < 10 and 0 <= c < 10

def bfs():
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while q:
        p = q.popleft()

        for i in range(4):
            next_r = p.r + dr[i]
            next_c = p.c + dc[i]

            if index_ok(next_r, next_c) and arr[next_r][next_c] != 'R' and dp[next_r][next_c] == 0:
                dp[next_r][next_c] = dp[p.r][p.c] + 1
                p2 = Push(next_r, next_c)
                q.append(p2)

if __name__ == "__main__":
    arr = [['' for _ in range(10)] for _ in range(10)]
    dp = [[0 for _ in range(10)] for _ in range(10)]
    q = deque()

    str_i = -1
    str_j = -1
    las_i = -1
    las_j = -1

    for i in range(10):
        row = input()
        for j in range(10):
            arr[i][j] = row[j]
            if arr[i][j] == 'B' or arr[i][j] == 'L':
                if str_i != -1:
                    las_i = i
                    las_j = j
                else:
                    str_i = i
                    str_j = j

    p = Push(str_i, str_j)
    q.append(p)
    bfs()

    print(dp[las_i][las_j] - 1)