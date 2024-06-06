N = int(input())

total = N + 1
for i in range(1, N + 1):
    init = i
    for j in range(1, N + 1):
        print(init, end = '')
        init = total - init
    print()