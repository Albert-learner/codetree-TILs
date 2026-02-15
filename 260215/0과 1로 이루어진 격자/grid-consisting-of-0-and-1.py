n = int(input())
grid = [list(input()) for _ in range(n)]

# Please write your code here.
a = [[1 if grid[i][j] == '1' else 0 for j in range(n)] for i in range(n)]

def flip(x, y):
    for i in range(x + 1):
        for j in range(y + 1):
            a[i][j] ^= 1

ans = 0

for i in range(n - 1, -1, -1):
    for j in range(n - 1, -1, -1):
        if a[i][j] == 1:
            flip(i, j)
            ans += 1

print(ans)
