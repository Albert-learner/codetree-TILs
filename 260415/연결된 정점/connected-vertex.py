n, m = map(int, input().split())

operations = []
for _ in range(m):
    op, *nums = input().split()
    if op == "x":
        a, b = map(int, nums)
        operations.append((op, a, b))
    else:
        a = int(nums[0])
        operations.append((op, a))

# Please write your code here.
parent = list(range(n + 1))
size = [1] * (n + 1)

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]

    return x

def union(a, b):
    fa = find(a)
    fb = find(b)

    if fa == fb:
        return

    if size[fa] < size[fb]:
        fa, fb = fb, fa

    parent[fb] = fa
    size[fa] += size[fb]

for op in operations:
    if op[0] == 'x':
        _, a, b = op
        union(a, b)
    else:
        _, a = op
        print(size[find(a)])