import copy

N, M, K = map(int, input().split())
miro = [list(map(int, input().split())) for _ in range(N)]
people = [list(map(lambda x: int(x) - 1, input().split())) for _ in range(M)]
exit_x, exit_y = map(lambda x: int(x) - 1, input().split())

move_dirs = {0: (-1, 0), 1: (1, 0), 2: (0, -1), 3: (0, 1)}
paths = 0

def move(paths):
    global people
    for p_num, (x, y) in enumerate(people):
        # row방향으로 얼마나 가야하는지, column방향으로 얼마나 가야하는지
        row, column = exit_x - x, exit_y - y

        # 움직이는 우선순위: row -> column / 그 방향이 벽이 아니어야 가능
        # row 먼저 check
        if row != 0:
            move = 1 if row > 0 else -1
            newpx, newpy = x + move, y
            if 0 <= newpx < N and 0 <= newpy < N and miro[newpx][newpy] == 0:
                people[p_num] = [newpx, newpy]
                paths += 1
                continue

        # 그 다음 column check
        if column != 0:
            move = 1 if column > 0 else -1
            newpx, newpy = x, y + move
            if 0 <= newpx < N and 0 <= newpy < N and miro[newpx][newpy] == 0:
                people[p_num] = [newpx, newpy]
                paths += 1

    return paths

def distance(x, y, p):
    # rotation을 위한 distance 계산

    row = int(abs(x - p[0]))
    column = int(abs(y - p[1]))
    d, r, c = max(row, column), min(x, p[0]), min(y, p[1])

    if row > column:
        # 변의 길이를 결정하는게 row라면 row는 그대로. column시작점을 옮길 수 있음
        c = max(y, p[1]) - d
        while c < 0:
            c += 1
        return d, r, c
    elif row < column:
        r = max(x, p[0]) - d
        while r < 0:
            r += 1
        return d, r, c
    else:
        return d, r, c


def rotate():
    global miro, people, exit_x, exit_y
    # 1. rotate할 위치 찾기
    distance_lst = []
    for person in people:
        distance_lst.append(distance(exit_x, exit_y, person))

    distance_lst = sorted(distance_lst)
    d, r, c = distance_lst[0]

    # 2. rotate하기
    tmp_miro = copy.deepcopy(miro)

    new_people = []
    new_exit_x, new_exit_y = exit_x, exit_y
    for i in range(d + 1):
        for j in range(d + 1):
            # 벽 -1
            if tmp_miro[r + i][c + j] > 0:
                tmp_miro[r + i][c + j] -= 1
            miro[r + j][c + d - i] = tmp_miro[r + i][c + j]
            while [r + i, c + j] in people:
                people.remove([r + i, c + j])
                new_people.append([r + j, c + d - i])
            if [r + i, c + j] == [exit_x, exit_y]:
                new_exit_x, new_exit_y = r + j, c + d - i

    people = people + new_people
    exit_x, exit_y = new_exit_x, new_exit_y

for _ in range(K):
    # 1. 움직이기
    paths = move(paths)

    # 2. exit으로 나간 것 정리
    while [exit_x, exit_y] in people:
        people.remove([exit_x, exit_y])

    if len(people) == 0:
        break

    rotate()

print(paths)
print(exit_x + 1, end=' ')
print(exit_y + 1)