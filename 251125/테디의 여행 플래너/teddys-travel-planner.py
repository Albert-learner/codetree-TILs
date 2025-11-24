N, Q = map(int, input().split())
cities = list(input().split())

option = []
new_city = [None] * Q

for i in range(Q):
    query = input().split()
    option.append(int(query[0]))
    if option[i] == 4:
        new_city[i] = query[1]

# Please write your code here.
class Node:
    __slots__ = ("name", "prev", "next")
    def __init__(self, name):
        self.name = name
        self.prev = None
        self.next = None

nodes = [Node(name) for name in cities]

if N > 0:
    for i in range(N):
        prev_i = (i - 1) % N
        next_i = (i + 1) % N
        nodes[i].prev = nodes[prev_i]
        nodes[i].next = nodes[next_i]
    cur = nodes[0]
    count = N
else:
    cur = None
    count = 0

out = []

def record_neighbors():
    if count <= 1 or cur is None:
        out.append("-1")
        return

    left_name = cur.prev.name
    right_name = cur.next.name
    if left_name == right_name:
        out.append("-1")
    else:
        out.append(f"{left_name} {right_name}")

for idx in range(Q):
    op = option[idx]

    if op == 1:
        if count > 1 and cur is not None:
            cur = cur.next

    elif op == 2:
        if count > 1 and cur is not None:
            cur = cur.prev

    elif op == 3:
        if count > 1 and cur is not None:
            target = cur.next
            if count == 2:
                cur.prev = cur
                cur.next = cur
            else:
                nxt = target.next
                cur.next = nxt
                nxt.prev = cur
            count -= 1
    elif op == 4:
        name = new_city[idx]
        new_node = Node(name)
        if cur is None:
            cur = new_node
            cur.prev = cur.next = cur
            count = 1
        else:
            if count == 0:
                cur = new_node
                cur.prev = cur.next = cur
                count = 1
            elif count == 1:
                new_node.prev = cur
                new_node.next = cur
                cur.prev = new_node
                cur.next = new_node
                count += 1
            else:
                right = cur.next
                new_node.prev = cur
                new_node.next = right
                cur.next = new_node
                right.prev = new_node
                count += 1

    record_neighbors()

print("\n".join(out))   