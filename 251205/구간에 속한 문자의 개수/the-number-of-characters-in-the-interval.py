n, m, k = map(int, input().split())

# Read grid as list of strings since we need character-by-character access
grid = [input() for _ in range(n)]

# Read k queries as tuples
queries = [tuple(map(int, input().split())) for _ in range(k)]

# Please write your code here.
for r1, c1, r2, c2 in queries:
    r1, c1 = r1 - 1, c1 - 1
    alp_cnts = {'a': 0, 'b': 0, 'c': 0}
    for r in range(r1, r2):
        for c in range(c1, c2):
            if grid[r][c] == 'a':
                alp_cnts['a'] += 1
            elif grid[r][c] == 'b':
                alp_cnts['b'] += 1
            elif grid[r][c] == 'c':
                alp_cnts['c'] += 1

    print(*alp_cnts.values())