N = int(input())
birds = sorted([tuple(map(int, input().split())) for _ in range(N)])

groups = []
cur_group = [birds[0]]
for i in range(1, len(birds)):
    if birds[i][0] == cur_group[0][0]:
        cur_group.append(birds[i])
    else:
        groups.append(cur_group)
        cur_group = [birds[i]]

cross_overs_min = 0
for group in groups:
    if len(group) % 2 == 0:
        poses = list(zip(*group))[1]
        zeros, ones = poses.count(0), poses.count(1)
        if zeros == ones:
            cross_overs_min += ones

print(cross_overs_min)