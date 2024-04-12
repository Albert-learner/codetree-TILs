N, M = map(int, input().split())
a_dist, b_dist = [0], [0]

def make_dist(player, p_dist):
    for i in range(player):
        velocity, times = map(int, input().split())
        for _ in range(times):
            p_dist.append(velocity + p_dist[-1])

make_dist(N, a_dist)
make_dist(M, b_dist)

cnts = 0
key = 0
prev_key = -100
for i in range(1, len(a_dist)):
    if a_dist[i] > b_dist[i]:
        key = -1
    elif a_dist[i] == b_dist[i]:
        key = 0
    else:
        key = 1

    if key != prev_key:
        cnts += 1

    prev_key = key

print(cnts)