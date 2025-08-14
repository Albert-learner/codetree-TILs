n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
visited = [[0] * n for _ in range(n)]
people, villages = 0, []

def can_go(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if visited[x][y] or grid[x][y] == 0:
        return False

    return True

def DFS(x, y):
    global people
    visited[x][y] = True
    people += 1

    move_dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dx, dy in move_dirs:
        mx, my = x + dx, y + dy
        if can_go(mx, my):
            DFS(mx, my)

for i in range(n):
    for j in range(n):
        if can_go(i, j):
            people = 0
            DFS(i, j)
            villages.append(people)

villages.sort()
print(len(villages))
for people in villages:
    print(people)