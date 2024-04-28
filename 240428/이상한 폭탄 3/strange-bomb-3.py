N, K = map(int, input().split())
bombs = [int(input()) for _ in range(N)]

last_idx = {}
explosions = {}

for i in range(N):
    if bombs[i] in last_idx:
        if i - last_idx[bombs[i]] <= K:
            explosions[bombs[i]] = explosions.get(bombs[i], 0) + 1

    last_idx[bombs[i]] = i

max_explosion = float("inf")
for idx in explosions.keys():
    if max_explosion == float("inf") or explosions[max_explosion] < explosions[idx]:
        max_explosion = idx
    elif explosions[max_explosion] == explosions[idx] and max_explosion < idx:
        max_explosion = idx

print(max_explosion if max_explosion != float("inf") else 0)