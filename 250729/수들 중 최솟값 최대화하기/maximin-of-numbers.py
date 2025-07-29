n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
from itertools import permutations

max_min_value = 0
for perm in permutations(range(n)):
    selected_values = [grid[row][perm[row]] for row in range(n)]
    min_value = min(selected_values)
    max_min_value = max(max_min_value, min_value)

print(max_min_value)