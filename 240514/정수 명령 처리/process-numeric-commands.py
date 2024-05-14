N = int(input())
cmds = []
for _ in range(N):
    cmd = input().split()
    if len(cmd) >= 2:
        cmds.append([cmd[0], int(cmd[1])])
    else:
        cmds.append(cmd)

stack = []
for cmd in cmds:
    if cmd[0] == "push":
        stack.append(cmd[1])
    elif cmd[0] == "size":
        print(len(stack))
    elif cmd[0] == "empty":
        print(1 if len(stack) == 0 else 0)
    elif cmd[0] == "pop":
        print(stack.pop())