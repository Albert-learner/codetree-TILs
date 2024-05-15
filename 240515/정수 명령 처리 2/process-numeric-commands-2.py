N = int(input())
queue = []
for _ in range(N):
    cmd = input().split()
    if cmd[0] == "push":
        queue.append(int(cmd[1]))
    elif cmd[0] == "front":
        print(queue[0])
    elif cmd[0] == "size":
        print(len(queue))
    elif cmd[0] == "empty":
        print(0 if len(queue) != 0 else 1)
    elif cmd[0] == "pop":
        print(queue.pop(0))