N = int(input())

plus, minus = 1, N
for i in range(1, N + 1):
    if i % 2 == 0:
        print("* " * plus)
        plus += 1
    else:
        print("* " * minus)
        minus -= 1

plus = (N // 2 + 1)
minus = N // 2

if N % 2 == 0:
    for i in range(1, N + 1):
        if i % 2 == 0:
            print("* " * plus)
            plus += 1
        else:
            print("* " * minus)
            minus -= 1
else:
    for i in range(1, N + 1):
        if i % 2 == 0:
            print("* " * minus)
            minus -= 1
        else:
            print("* " * plus)
            plus += 1