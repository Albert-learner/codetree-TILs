S_init = input()
N = int(input())

commands = []
S_values = []

for _ in range(N):
    line = input().split()
    cmd = int(line[0])
    commands.append(cmd)
    if cmd == 1 or cmd == 2:
        S_values.append(line[1])
    else:
        S_values.append("")

# Please write your code here.
class Node:
    def __init__(self, val: str):
        self.val = val
        self.prev = None
        self.next = None

cur = Node(S_init)

out_lines = []

for cmd, sval in zip(commands, S_values):
    if cmd == 1:
        new_node = Node(sval)
        new_node.prev = cur.prev
        new_node.next = cur
        if cur.prev is not None:
            cur.prev.next = new_node
        cur.prev = new_node

    elif cmd == 2:
        new_node = Node(sval)
        new_node.next = cur.next
        new_node.prev = cur
        if cur.next is not None:
            cur.next.prev = new_node
        cur.next = new_node

    elif cmd == 3:
        if cur.prev is not None:
            cur = cur.prev

    elif cmd == 4:
        if cur.next is not None:
            cur = cur.next

    prev_val = cur.prev.val if cur.prev is not None else "(Null)"
    cur_val = cur.val
    next_val = cur.next.val if cur.next is not None else "(Null)"
    out_lines.append(f"{prev_val} {cur_val} {next_val}")

print("\n".join(out_lines))






