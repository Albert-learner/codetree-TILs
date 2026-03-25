n = int(input())

# Initialize arrays with n+1 size to match 1-based indexing
t = [0] * (n + 1)
a = [0] * (n + 1)
p = [0] * (n + 1)

# Process input for nodes 2 to n
children = [[] for _ in range(n + 1)]

for i in range(2, n + 1):
    t[i], a[i], p[i] = map(int, input().split())
    children[p[i]].append(i)

# Please write your code here.
value = [0] * (n + 1)

order = []
stack = [1]

while stack:
    cur = stack.pop()
    order.append(cur)
    for nxt in children[cur]:
        stack.append(nxt)

for cur in reversed(order):
    child_sum = 0
    for nxt in children[cur]:
        child_sum += value[nxt]

    if cur == 1:
        value[cur] = child_sum
    else:
        own = a[cur] if t[cur] == 1 else -a[cur]
        total = own + child_sum
        value[cur] = max(0, total)

print(value[1])