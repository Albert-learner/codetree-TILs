n = int(input())
parent = list(map(int, input().split()))
remove_node = int(input())

# Please write your code here.
children = [[] for _ in range(n)]
root = -1

for i in range(n):
    if parent[i] == -1:
        root = i
    else:
        children[parent[i]].append(i)

if remove_node == root:
    print(0)
else:
    removed = [False] * n

    stack = [remove_node]
    removed[remove_node] = True
    while stack:
        cur = stack.pop()
        for nxt in children[cur]:
            removed[nxt] = True
            stack.append(nxt)

    leaf_count = 0
    for i in range(n):
        if removed[i]:
            continue

        has_child = False
        for nxt in children[i]:
            if not removed[nxt]:
                has_child = True
                break

        if not has_child:
            leaf_count += 1

    print(leaf_count)