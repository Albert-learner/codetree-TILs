n = int(input())
commands = []
for _ in range(n):
    line = input().split()
    cmd = line[0]
    k = int(line[1])
    if cmd == "add":
        v = int(line[2])
        commands.append((cmd, k, v))
    else:
        commands.append((cmd, k))

# Please write your code here.
hashmap = {}
for one_cmd in commands:
    if len(one_cmd) == 3:
        cmd, k, v = one_cmd[0], int(one_cmd[1]), int(one_cmd[2])
        hashmap[k] = v
    else:
        if(one_cmd[0]) == "find":
            k = int(one_cmd[1])
            if k in hashmap.keys():
                print(hashmap[k])
            else:
                print(None)
        else:
            k = int(one_cmd[1])
            del hashmap[k]

