N = int(input())
commands = []

for _ in range(N):
    line = input().split()
    if line[0] == "push":
        commands.append((line[0], int(line[1])))
    else:
        commands.append((line[0],))

# Please write your code here.
queue = []
for cmd in commands:
    if cmd[0] == "push":
        queue.append(cmd[1])
    elif cmd[0] == "pop":
        max_cst = max(queue)
        print(max_cst)
        queue.pop(queue.index(max_cst))
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        print(1 if len(queue) == 0 else 0)
    elif cmd[0] == "top":
        print(max(queue))