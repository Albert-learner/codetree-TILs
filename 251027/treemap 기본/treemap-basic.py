n = int(input())

cmd = []
k = []
v = []

for _ in range(n):
    line = input().split()
    cmd.append(line[0])
    if line[0] == "add":
        k.append(int(line[1]))
        v.append(int(line[2]))
    elif line[0] == "remove" or line[0] == "find":
        k.append(int(line[1]))
        v.append(0)
    else:
        k.append(0)
        v.append(0)

# Please write your code here.
mp = {}

out_lines = []
for i in range(n):
    c = cmd[i]
    key = k[i]
    val = v[i]

    if c == "add":
        mp[key] = val

    elif c == "remove":
        # key exists per problem statement
        mp.pop(key, None)

    elif c == "find":
        out_lines.append(str(mp[key]) if key in mp else "None")

    elif c == "print_list":
        if not mp:
            out_lines.append("None")
        else:
            # sort by key, print values in that order
            vals = [mp[x] for x in sorted(mp.keys())]
            out_lines.append(" ".join(map(str, vals)))

print("\n".join(out_lines))