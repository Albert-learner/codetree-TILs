from collections import deque

def in_range(r, c, N):
    return 0 <= r < N and 0 <= c < N

def init(N, map, check):
    temp = [row[:] for row in map]
    for i in range(N):
        for j in range(N):
            for d in range(4):
                check[i][j][d] = False
    column_set = set()
    return temp, column_set

def find_answer(N, temp, check):
    cnt = 0
    r_arr = [-1, 1, 0, 0]
    c_arr = [0, 0, -1, 1]
    turn = [1, 0, 3, 2]
    
    for i in range(N):
        for j in range(N):
            if temp[i][j] == 0:
                continue
            for d in range(4):
                nr = i + r_arr[d]
                nc = j + c_arr[d]
                if not in_range(nr, nc, N) or check[i][j][d]:
                    continue
                check[i][j][d] = True
                check[nr][nc][turn[d]] = True
                if temp[i][j] == temp[nr][nc]:
                    cnt += 1
    return cnt

def down(N, temp, column_set):
    r_arr = [-1, 1, 0, 0]
    c_arr = [0, 0, -1, 1]
    que = deque()
    
    for c in column_set:
        for r in range(N-1, -1, -1):
            if temp[r][c] != 0:
                que.append(temp[r][c])
                temp[r][c] = 0
        row_idx = N - 1
        while que:
            temp[row_idx][c] = que.popleft()
            row_idx -= 1
    return temp

def bomb(N, temp, r, c, column_set):
    r_arr = [-1, 1, 0, 0]
    c_arr = [0, 0, -1, 1]
    length = temp[r][c] - 1
    temp[r][c] = 0
    column_set.add(c)

    for d in range(4):
        for i in range(1, length + 1):
            nr = r + r_arr[d] * i
            nc = c + c_arr[d] * i
            if not in_range(nr, nc, N):
                break
            temp[nr][nc] = 0
            column_set.add(nc)
    return temp, column_set

def process(N, map):
    check = [[[False] * 4 for _ in range(N)] for _ in range(N)]
    ans = 0

    for i in range(N):
        for j in range(N):
            temp, column_set = init(N, map, check)
            temp, column_set = bomb(N, temp, i, j, column_set)
            temp = down(N, temp, column_set)
            cnt = find_answer(N, temp, check)
            ans = max(ans, cnt)
    return ans

def input_data():
    import sys
    input = sys.stdin.read
    data = input().split()
    N = int(data[0])
    map = []
    index = 1
    for i in range(N):
        row = []
        for j in range(N):
            row.append(int(data[index]))
            index += 1
        map.append(row)
    return N, map

def output(ans):
    print(ans)

def main():
    N, map = input_data()
    ans = process(N, map)
    output(ans)

if __name__ == "__main__":
    main()