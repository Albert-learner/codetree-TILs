n = int(input())
words = input().split()
board = [list(input()) for _ in range(4)]

# Please write your code here.
child = [{}]
end_word = [False]

def insert(word):
    node = 0

    for ch in word:
        if ch not in child[node]:
            child[node][ch] = len(child)
            child.append({})
            end_word.append(False)

        node = child[node][ch]

    end_word[node] = True

for word in words:
    insert(word)

answer = 0

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

visited = [[False] * 4 for _ in range(4)]

def dfs(x, y, node, length):
    global answer

    if end_word[node]:
        answer = max(answer, length)

    if length == 8:
        return

    visited[x][y] = True

    for d in range(8):
        nx = x + dx[d]
        ny = y + dy[d]

        if not (0 <= nx < 4 and 0 <= ny < 4):
            continue

        if visited[nx][ny]:
            continue

        ch = board[nx][ny]

        if ch not in child[node]:
            continue

        dfs(nx, ny, child[node][ch], length + 1)

    visited[x][y] = False

for i in range(4):
    for j in range(4):
        ch = board[i][j]

        if ch in child[0]:
            dfs(i, j, child[0][ch], 1)

print(answer)