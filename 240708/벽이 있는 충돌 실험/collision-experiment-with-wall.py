T = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def parse_key(key):
    return list(map(int, key.split(',')))

def make_key(x, y):
    return f"{x},{y}"

def get_direc(direct):
    if direct == 'U':
        return 0
    elif direct == 'D':
        return 1
    elif direct == 'L':
        return 2
    else:
        return 3

def turn_direc(direc):
    if direc == 0:
        return 1
    elif direc == 1:
        return 0
    elif direc == 2:
        return 3
    else:
        return 2

def is_range(x, y):
    return 0 <= x < N and 0 <= y < N

results = []
for _ in range(T):
    N, M = map(int, input().split())
    
    map_dict = {}
    for _ in range(M):
        x, y, d = input().split()
        x, y = int(x) - 1, int(y) - 1
        direct = get_direc(d)

        map_dict[make_key(y, x)] = direct

    sec = 0
    while sec <= 2 * N:
        sec += 1
        board = [[0] * N for _ in range(N)]
        renew_map = {}

        for key in map_dict.keys():
            pos = parse_key(key)
            x, y = pos
            direct = map_dict[key]

            mx, my = x + dx[direct], y + dy[direct]

            if is_range(mx, my):
                board[mx][my] += 1

                if board[mx][my] > 1:
                    renew_map.pop(make_key(mx, my), None)
                else:
                    renew_map[make_key(mx, my)] = direct
            else:
                board[y][x] += 1

                if board[y][x] > 1:
                    renew_map.pop(make_key(x, y), None)
                else:
                    renew_map[make_key(x, y)] = turn_direc(direct)
                    
        map_dict = renew_map

    answer = len(map_dict)
    results.append(str(answer))

for result in results:
    print(result)