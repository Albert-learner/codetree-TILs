T = int(input())

for _ in range(T):
    k = int(input())
    operations = [tuple(input().split()) for _ in range(k)]
    commands = [op[0] for op in operations]
    ns = [int(op[1]) for op in operations]

    # Please write your code here.
    queue = []
    for cmd, n in zip(commands, ns):
        if cmd == "I":
            queue.append(n)
        elif cmd == "D":
            if n == 1:
                if len(queue) != 0:
                    max_cst = max(queue)
                    queue.remove(max_cst)
            elif n == -1:
                if len(queue) != 0:
                    min_cst = min(queue)
                    queue.remove(min_cst)
                else:
                    print("EMPTY")

    if len(queue) != 0:
        print(max(queue), min(queue))
    else:
        print("EMPTY")