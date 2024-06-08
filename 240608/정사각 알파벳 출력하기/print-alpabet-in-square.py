N = int(input())

start_chr = ord('A')
for i in range(N):
    for j in range(N):
        print(chr(start_chr + i * N + j), end = '')
    print()