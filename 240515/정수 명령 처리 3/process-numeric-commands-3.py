from collections import deque

N = int(input())
dque = deque()
for _ in range(N):
    cmd = input().split()
    if cmd[0] == "push_back":
        dque.append(int(cmd[1]))
    elif cmd[0] == "push_front":
        dque.appendleft(int(cmd[1]))
    elif cmd[0] == "pop_front":
        print(dque.popleft())
    elif cmd[0] == "pop_back":
        print(dque.pop())
    elif cmd[0] == "front":
        print(dque[0])
    elif cmd[0] == "size":
        print(len(dque))
    elif cmd[0] == "empty":
        print(1 if len(dque) == 0 else 0)
    elif cmd[0] == "back":
        print(dque[-1])