n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def press(r, c):
    for dr, dc in [(0, 0), (-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < n and 0 <= nc < n:
            arr[nr][nc] ^= 1

ans = 0

for r in range(1, n):
    for c in range(n):
        if arr[r - 1][c] == 0:
            press(r, c)
            ans += 1

ok = all(arr[i][j] == 1 for i in range(n) for j in range(n))
print(ans if ok else -1)