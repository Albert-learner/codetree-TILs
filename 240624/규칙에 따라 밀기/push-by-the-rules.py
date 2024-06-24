a_str = input()
cmds = input()

for cmd in cmds:
    if cmd == 'L':
        a_str = a_str[1:] + a_str[0]
    elif cmd == 'R':
        a_str = a_str[-1] + a_str[:-1]

print(a_str)