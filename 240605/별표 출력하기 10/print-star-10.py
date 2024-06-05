N = int(input())

for i in range(N * 2):
    if i % 2 == 1:
        print("* " * (N - (i - 1) // 2))
    else:
        print("* " * (1 + (i // 2)))