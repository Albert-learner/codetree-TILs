n = int(input())
commands = []
xs = []

for _ in range(n):
    line = input().split()
    commands.append(line[0])
    if line[0] in ["add", "remove", "find", "lower_bound", "upper_bound"]:
        xs.append(int(line[1]))
    else:
        xs.append(0)

# Please write your code here.
from sortedcontainers import SortedSet

sort_set = SortedSet()
for cmd, x in zip(commands, xs):
    if cmd == "add":
        sort_set.add(x)
    elif cmd == "remove":
        sort_set.remove(x)
    elif cmd == "find":
        print("true" if x in sort_set else "false")
    elif cmd == "lower_bound":
        l_idx = sort_set.bisect_left(x)
        print(sort_set[l_idx] if l_idx < len(sort_set) else "None")         
    elif cmd == "upper_bound":
        u_idx = sort_set.bisect_right(x)
        print(sort_set[u_idx] if u_idx < len(sort_set) else "None")
    elif cmd == "largest":
        print(sort_set[-1] if sort_set else "None") 
    elif cmd == "smallest":
        print(sort_set[0] if sort_set else "None")