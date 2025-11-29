n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
ps = [[0] * (n + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(n):
        ps[i + 1][j + 1] = (
            ps[i][j + 1] + ps[i + 1][j] - ps[i][j] + arr[i][j]
        )

max_sum = 0

for i in range(n - k + 1):       
    for j in range(n - k + 1):
        total = (
            ps[i + k][j + k]
            - ps[i][j + k]
            - ps[i + k][j]
            + ps[i][j]
        )
        if total > max_sum:
            max_sum = total

print(max_sum)