N = int(input())

start_chr = ord('A')
for i in range(N):
    for j in range(N):
        start_chr += j
        print(chr(start_chr), end = '')
    print()