N, K = map(int, input().split())
bombs = [int(input()) for _ in range(N)]

explosions = dict.fromkeys(set(bombs), 0)
for f_idx in range(N - K + 1):
    for r_idx in range(f_idx + 1, N):
        if abs(r_idx - f_idx) <= K and bombs[f_idx] == bombs[r_idx] and not explosions[bombs[f_idx]]:
            explosions[bombs[f_idx]] = 1
        elif abs(r_idx - f_idx) <= K and bombs[f_idx] == bombs[r_idx] and explosions[bombs[f_idx]] >= 1:
            explosions[bombs[f_idx]] += 1

max_explosion = max(explosions.values())
explosions_sort = dict(sorted(explosions.items(), key=lambda x: x[1], reverse=True))
max_bombs = []
for bomb, explosion_cnts in explosions_sort.items():
    if explosion_cnts == max_explosion:
        max_bombs.append(bomb)

print(sorted(max_bombs, reverse=True)[0])