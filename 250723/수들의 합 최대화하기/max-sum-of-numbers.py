n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [False] * n
max_sum = 0

def simulation(cur, p_sum):
    global max_sum

    if cur == n:
        max_sum = max(max_sum, p_sum)
        return

    for col in range(n):
        if visited[col]:
            continue

        visited[col] = True
        simulation(cur + 1, p_sum + grid[cur][col])
        visited[col] = False

simulation(0, 0)
print(max_sum)