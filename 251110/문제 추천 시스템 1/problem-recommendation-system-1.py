n = int(input())
P, L = [], []
for _ in range(n):
    p, l = map(int, input().split())
    P.append(p)
    L.append(l)

m = int(input())
commands = []
for _ in range(m):
    cmd = input().split()
    if cmd[0] == "rc":
        commands.append((cmd[0], int(cmd[1])))
    else:
        commands.append((cmd[0], int(cmd[1]), int(cmd[2])))

# Please write your code here.
import bisect

matters = [(l, p) for p, l in zip(P, L)]
bisect.insort(matters, (l, p))

for line in commands:
    if line[0] == "ad":
        bisect.insort(matters, (line[2], line[1]))
    elif line[0] == "sv":
        matters.remove((line[2], line[1]))
    else:
        print(matters[0][1] if line[1] == -1 else matters[-1][1])
