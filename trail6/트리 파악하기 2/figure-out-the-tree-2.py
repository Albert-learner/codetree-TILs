n = int(input())
nodes = []
k = []

for _ in range(n):
    line = input().split()
    k.append(int(line[0]))
    nodes.append(list(line[1:]))

# Please write your code here.
tree = {}

for path in nodes:
    cur = tree

    for name in path:
        if name not in cur:
            cur[name] = {}
        cur = cur[name]

answer = []
def DFS(cur, depth):
    for name in sorted(cur.keys()):
        answer.append("--" * depth + name)
        DFS(cur[name], depth + 1)

DFS(tree, 0)

print("\n".join(answer))