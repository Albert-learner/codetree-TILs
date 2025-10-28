n = int(input())
commands = []
x = []
for _ in range(n):
    cmd, val = input().split()
    commands.append(cmd)
    x.append(int(val))

# Please write your code here.
hashset = set()
for cmd, x_val in zip(commands, x):
    if cmd == "find":
        if x_val in hashset:
            print("true")
        else:
            print("false")
    elif cmd == "add":
        hashset.add(x_val)
    elif cmd == "remove":
        hashset.remove(x_val)