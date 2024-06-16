from collections import deque

def get_max_gold(start_y, start_x, n, gold_price, board):
    max_gold = 0
    visited = [[False] * n for _ in range(n)]
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    for k in range(n):
        for i in range(n):
            visited[i] = [False] * n

        visited[start_y][start_x] = True
        bfs = deque([(start_y, start_x, 0)])
        total_gold_acquired = 0

        while bfs:
            y, x, step = bfs.popleft()

            if k < step:
                break

            total_gold_acquired += board[y][x]

            for i in range(4):
                ny, nx = y + dy[i], x + dx[i]

                if ny < 0 or nx < 0 or ny >= n or nx >= n:
                    continue

                if visited[ny][nx]:
                    continue

                visited[ny][nx] = True
                bfs.append((ny, nx, step + 1))

        cost = k * k + (k + 1) * (k + 1)
        if cost <= total_gold_acquired * gold_price:
            max_gold = max(max_gold, total_gold_acquired)

    return max_gold

def main():
    n, gold_price = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    max_gold = 0

    for y in range(n):
        for x in range(n):
            max_gold = max(max_gold, get_max_gold(y, x, n, gold_price, board))

    print(max_gold)

if __name__ == "__main__":
    main()