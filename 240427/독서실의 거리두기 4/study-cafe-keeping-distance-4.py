N = int(input())
seats = list(input())

max_dist = 0
for i in range(N):
    if seats[i] == '1':
        continue

    dist = float("inf")
    fill_poses = [j for j in range(N) if seats[j] == '1' or i == j]
    for j in range(len(fill_poses) - 1):
        dist = min(dist, fill_poses[j + 1] - fill_poses[j])

    max_dist = max(max_dist, dist)

print(max_dist)