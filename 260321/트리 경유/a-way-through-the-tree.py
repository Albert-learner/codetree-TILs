n, q = map(int, input().split())
dest = [int(input()) for _ in range(q)]

# Please write your code here.
occupied = set()

for x in dest:
    path = []
    cur = x

    while cur >= 1:
        path.append(cur)
        cur //= 2

    path.reverse()
    blocked = 0
    for node in path:
        if node in occupied:
            blocked = node
            break

    print(blocked)

    if blocked == 0:
        occupied.add(x)