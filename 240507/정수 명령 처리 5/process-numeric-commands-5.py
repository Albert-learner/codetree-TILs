N = int(input())
d_lst = []
for _ in range(N):
    cmd = input().split()
    if cmd[0] == "push_back":
        size = int(cmd[1])
        d_lst.append(size)
    elif cmd[0] == "get":
        size = int(cmd[1])
        print(d_lst[size - 1])
    elif cmd[0] == "size":
        print(len(d_lst))
    elif cmd[0] == "pop_back":
        d_lst.pop()