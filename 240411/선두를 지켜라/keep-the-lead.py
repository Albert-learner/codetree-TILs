N, M = map(int, input().split())
a_moves = [list(map(int, input().split())) for _ in range(N)]
b_moves = [list(map(int, input().split())) for _ in range(M)]


a_pos, b_pos = [0], [0]
for (a_vel, a_times), (b_vel, b_times) in zip(a_moves, b_moves):
    a_dist, b_dist = a_vel * a_times, b_vel * b_times
    a_pos.append(a_dist)
    b_pos.append(b_dist)

change_cnts = 0
front_runner = 'A' if a_pos[1] > b_pos[1] else 'B' if a_pos[1] < b_pos[1] else ''
for a_dist, b_dist in zip(a_pos[1:], b_pos[1:]):
    if a_dist > b_dist and front_runner == 'A':
        continue
    elif a_dist < b_dist and front_runner == 'A':
        change_cnts += 1
        front_runner = 'B'
    elif a_dist > b_dist and front_runner == 'B':
        change_cnts += 1
        front_runner = 'A'
    elif a_dist < b_dist and front_runner == 'B':
        continue

print(change_cnts)