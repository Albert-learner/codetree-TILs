T = int(input())

for _ in range(T):
    k = int(input())
    operations = [tuple(input().split()) for _ in range(k)]
    commands = [op[0] for op in operations]
    ns = [int(op[1]) for op in operations]

    # Please write your code here.
    from sortedcontainers import SortedSet

    sort_set = SortedSet()
    for cmd, n in zip(commands, ns):
        if cmd == "I":
            sort_set.add(n)
        elif cmd == "D":
            if n == 1:
                if len(sort_set) != 0:
                    sort_set.remove(sort_set[-1])
            elif n == -1:
                if len(sort_set) != 0:
                    sort_set.remove(sort_set[0])
                else:
                    print("EMPTY")

    if len(sort_set) != 0:
        print(sort_set[-1], sort_set[0])
    else:
        print("EMPTY")