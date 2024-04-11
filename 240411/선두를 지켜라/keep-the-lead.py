N, M = map(int, input().split())
a_dist, b_dist = [0], [0]

def make_dist(p_num, which_dist):
    for i in range(p_num):
        velocity, times = map(int, input().split())
        for j in range(times):
            which_dist.append(velocity + which_dist[-1])

make_dist(N, a_dist)
make_dist(M, b_dist)

compare = [a_dist[i] - b_dist[i] for i in range(len(a_dist)) if a_dist[i] != b_dist[i]]

answer = 0
for i in range(1, len(compare)):
    if compare[i] * compare[i - 1] < 0:
        answer += 1

print(answer)