N, M = map(int, input().split())
a_moves = [list(map(int, input().split())) for _ in range(N)]
b_moves = [list(map(int, input().split())) for _ in range(M)]

a_first, b_first = a_moves[0], b_moves[0]
change_cnts = 0
front_runner = 'A' if a_first[0] > b_first[0] else 'B' if a_first[0] < b_first[0] else ''
for (a_vel, _), (b_vel, _) in zip(a_moves[1:], b_moves[1:]):
    if a_vel > b_vel and front_runner == 'A':
        continue
    elif a_vel < b_vel and front_runner == 'A':
        change_cnts += 1
        front_runner = 'B'
    elif a_vel > b_vel and front_runner == 'B':
        change_cnts += 1
        front_runner = 'A'
    elif a_vel < b_vel and front_runner == 'B':
        continue

print(change_cnts)