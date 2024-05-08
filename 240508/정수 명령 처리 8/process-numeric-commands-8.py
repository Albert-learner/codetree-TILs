N = int(input())

d_lst = []
for _ in range(N):
    cmd = input().split()
    if cmd[0] == "push_back":
        d_lst.append(int(cmd[1]))
    elif cmd[0] == "push_front":
        d_lst.insert(0, int(cmd[1]))
    elif cmd[0] == "pop_front":
        print(d_lst.pop(0))
    elif cmd[0] == "pop_back":
        print(d_lst.pop())
    elif cmd[0] == "front":
        print(d_lst[0])
    elif cmd[0] == "back":
        print(d_lst[-1])
    elif cmd[0] == "size":
        print(len(d_lst))
    elif cmd[0] == "empty":
        print(1 if len(d_lst) == 0 else 0)