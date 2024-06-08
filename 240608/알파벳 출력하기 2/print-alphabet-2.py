N = int(input())

cur_chr = ord('A')
for i in range(N):
    print(' ' * (2 * i), end = '')

    for j in range(N - i):
        print(chr(cur_chr), end = ' ')
        cur_chr += 1
        if cur_chr > ord('Z'):
            cur_chr = ord('A')
        
    print()