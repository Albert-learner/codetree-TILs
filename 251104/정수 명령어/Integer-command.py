from sortedcontainers import SortedSet

T = int(input())

for _ in range(T):
    k = int(input())

    s = SortedSet()
    for _ in range(k):
        op, x = input().split()
        x = int(x)

        if op == 'I':
            s.add(x)
        else: 
            if not s:
                continue
            if x == 1:
                s.remove(s[-1])
            else:
                s.remove(s[0]) 

    if s:
        print(s[-1], s[0])
    else:
        print("EMPTY")
