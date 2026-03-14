n, k = map(int, input().split())
sequence = list(map(int, input().split()))

# Please write your code here.
parent = {}
root = sequence[0]
parent[root] = 0

groups = []
start = 0
for i in range(1, n):
    if sequence[i] != sequence[i - 1] + 1:
        groups.append(sequence[start:i])
        start = i
groups.append(sequence[start:n])

parent_idx = 0
for gi in range(1, len(groups)):
    p = sequence[parent_idx]
    for x in groups[gi]:
        parent[x] = p
    parent_idx += 1

k_parent = parent[k]
if k_parent == 0:
    print(0)
else:
    k_grand = parent[k_parent]
    if k_grand == 0:
        print(0)
    else:
        answer = 0
        for x in sequence:
            if x == k:
                continue
            px = parent[x]
            if px == 0:
                continue
            gx = parent[px]
            if gx == k_grand and px != k_parent:
                answer += 1
        print(answer)