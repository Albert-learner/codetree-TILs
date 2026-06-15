n = int(input())
words = []
k = []

for _ in range(n):
    line = input().split()
    k.append(int(line[0]))
    words.append(line[1:])

# Please write your code here.
tree = {}

for path in words:
    cur = tree

    for node in path:
        if node not in cur:
            cur[node] = {}
        cur = cur[node]

def dfs(cur, depth):
    for name in sorted(cur.keys()):
        print("--" * depth + name)
        dfs(cur[name], depth + 1)

dfs(tree, 0)

