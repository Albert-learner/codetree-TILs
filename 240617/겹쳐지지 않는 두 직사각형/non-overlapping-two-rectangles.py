N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

def get_space1(y1, x1, h1, w1, board, paper):
    space1 = 0
    for y in range(y1, y1 + h1):
        for x in range(x1, x1 + w1):
            space1 += board[y][x]
            paper[y][x] = 1

    return space1

def get_space2(y2, x2, h2, w2, board, paper):
    space2 = 0
    for y in range(y2, y2 + h2):
        for x in range(x2, x2 + w2):
            if paper[y][x] == 1:
                return -999
            space2 += board[y][x]

    return space2

def reset_paper(height, width):
    return [[0] * width for _ in range(height)]

max_areas = -float("INF")
space1, space2 = 0, 0
for y1 in range(N):
    for x1 in range(M):
        for h1 in range(1, N - y1 + 1):
            for w1 in range(1, M - x1 + 1):
                paper = reset_paper(N, M)
                space1 = get_space1(y1, x1, h1, w1, board, paper)
                
                for y2 in range(N):
                    for x2 in range(M):
                        for h2 in range(1, N - y2 + 1):
                            for w2 in range(1, M - x2 + 1):
                                space2 = get_space2(y2, x2, h2, w2, board, paper)

                                if space2 == -999:
                                    continue

                                max_areas = max(max_areas, space1 + space2)

print(max_areas)