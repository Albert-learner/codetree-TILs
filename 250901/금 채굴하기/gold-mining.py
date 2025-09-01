n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
max_golds = 0

def mining_costs(k):
    return k ** 2 + (k + 1) ** 2

def get_nums_of_golds(r, c, k):
    return sum([grid[i][j] for i in range(n) for j in range(n) if abs(r - i) + abs(c - j) <= k])

for i in range(n):
    for j in range(n):
        for r_size in range(2 * (n - 1) + 1):
            golds = get_nums_of_golds(i, j, r_size)

            if golds * m >= mining_costs(r_size):
                max_golds = max(max_golds, golds)

print(max_golds)