n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
def mining_costs(k):
    return k ** 2 + (k + 1) ** 2

def get_num_of_golds(row, col, k):
    return sum([grid[i][j] for i in range(n) for j in range(n) if abs(row - i) + abs(col - j) <= k])

max_golds = 0
for i in range(n):
    for j in range(n):
        for s_size in range(2 * (n - 1) + 1):
            golds = get_num_of_golds(i, j, s_size)

            if golds * m >= mining_costs(s_size):
                max_golds = max(max_golds, golds)

print(max_golds)