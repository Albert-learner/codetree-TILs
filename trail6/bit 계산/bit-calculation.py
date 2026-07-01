q = int(input())
commands = []
for _ in range(q):
    line = input().split()
    if line[0] != "clear":
        commands.append((line[0], int(line[1])))
    else:
        commands.append((line[0],))

# Please write your code here.
S = 0
output = []
for command in commands:
    if command[0] != "clear":   
        cmd, x = command
        if cmd == "add":
            S |= (1 << x)
        elif cmd == "delete":
            S &= ~(1 << x)
        elif cmd == "print":
            output.append(1 if S & (1 << x) else 0)
        elif cmd == "toggle":
            S ^= (1 << x)
    else:
        S = 0

print('\n'.join(map(str, output)))