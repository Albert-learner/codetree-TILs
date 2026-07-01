q = int(input())
commands = []
for _ in range(q):
    line = input().split()
    if line[0] != "clear":
        commands.append((line[0], int(line[1])))
    else:
        commands.append((line[0],))

# Please write your code here.
S_set = set()
for command in commands:
    if command[0] != "clear":
        cmd, cst = command
        if cmd == "add":
            if cst not in S_set:
                S_set.add(cst)
        elif cmd == "delete":
            if cst in S_set:
                S_set.discard(cst)
        elif cmd == "print":
            if cst in S_set:
                print(1)
            else:
                print(0)
        elif cmd == "toggle":
            if cst in S_set:
                S_set.discard(cst)
            else:
                S_set.add(cst)
    else:
        S_set.clear()
