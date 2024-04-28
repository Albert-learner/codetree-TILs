N, K = map(int, input().split())
bombs = [int(input()) for _ in range(N)]

max_explosions = 0
for f_idx in range(N):
    explosions = 0
    for r_idx in range(f_idx + 1, N):
        if abs(r_idx - f_idx) <= K and bombs[f_idx] == bombs[r_idx]:
            explosions += 1

    max_explosions = max(max_explosions, explosions)

print(max_explosions)