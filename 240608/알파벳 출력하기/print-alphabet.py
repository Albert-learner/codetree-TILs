N = int(input())

cur_chr = ord('A')
for i in range(1, N + 1):
    for j in range(i):
        print(chr(cur_chr), end = '')
        cur_chr += 1
        if cur_chr > ord('Z'):
            cur_chr = ord('A')
    print()