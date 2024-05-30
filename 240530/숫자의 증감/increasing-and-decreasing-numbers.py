input_chr, N = input().split()
N = int(N)

if input_chr == 'A':
    for i in range(1, N + 1):
        print(i, end = ' ')
else:
    for i in range(N, 0, -1):
        print(i, end = ' ')