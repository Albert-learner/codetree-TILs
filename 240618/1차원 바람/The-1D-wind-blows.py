from collections import deque

def BFS(r, d, start):
    que = deque()
    que.append([r, d, start])
    while que:
        r, d, start = que.popleft()
        select_row = building[r]
        select_row = deque(select_row)
        select_row.rotate(d)
        building[r] = list(select_row)

        if r - 1 >= 0 and start >= 0:
            for i in range(M):
                if building[r][i] == building[r - 1][i]:
                    que.append([r - 1, -d, 1])
                    break
        
        if r + 1 < N and start <= 0:
            for i in range(M):
                if building[r][i] == building[r + 1][i]:
                    que.append([r + 1, -d, -1])
                    break

N, M, Q = map(int, input().split())
building = [list(map(int, input().split())) for _ in range(N)]
for _ in range(Q):
    row_num, direction = input().split()
    direct = 0
    if direction == 'L':
        direct = 1
    else:
        direct = -1
    
    BFS(int(row_num) - 1, direct, 0)

for row in building:
    print(*row)