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

# # 모범답안
# n = 10
# board = [
#     input()
#     for _ in range(n)
# ]
    
# # L, R, B의 위치를 찾습니다.
# for i in range(n):
#     for j in range(n):
#         if board[i][j] == 'L':
#             l_x = i
#             l_y = j
#         if board[i][j] == 'R':
#             r_x = i
#             r_y = j
#         if board[i][j] == 'B':
#             b_x = i
#             b_y = j

# # Case 1 : L과 B가 일직선상에 없다면, 반드시 L에서 B를 가는 최단경로중에
# # R을 피해서 갈 수 있는 경로가 있습니다.
# # 따라서 L과 B가 일직선상이 아니라면 L과 B의 최단경로를 구해주면 됩니다.
# if l_x != b_x and l_y != b_y:
#     print(abs(l_x - b_x) + abs(l_y - b_y) - 1)

# # Case 2 : L과 B가 세로 방향으로 일직선상에 있다면,
# # 그 일직선 사이에 R이 있을 때에는 2칸 돌아갑니다.
# # 그 외의 모든 경우에 대해 L과 B의 최단경로를 그대로 구해주면 됩니다.
# elif l_y == b_y:
#     if l_y == r_y and r_x >= min(b_x, l_x) and r_x <= max(b_x, l_x):
#         print(abs(l_x - b_x) + abs(l_y - b_y) + 1)
#     else:
#         print(abs(l_x - b_x) + abs(l_y - b_y) - 1)

# # Case 3 : L과 B가 가로 방향으로 일직선상에 있다면,
# # 그 일직선 사이에 R이 있을 때에는 2칸 돌아갑니다.
# # 그 외의 모든 경우에 대해 L과 B의 최단경로를 그대로 구해주면 됩니다.
# elif l_x == b_x:
#     if l_x == r_x and r_y >= min(b_y, l_y) and r_y <= max(b_y, l_y):
#         print(abs(l_x - b_x) + abs(l_y - b_y) + 1)
#     else:
#         print(abs(l_x - b_x) + abs(l_y - b_y) - 1)