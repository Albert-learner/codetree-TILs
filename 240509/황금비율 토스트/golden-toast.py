N, M = map(int, input().split())
word = input()
word_lst = list(word)
codes = [input().split() for _ in range(M)]

itr = N
for code in codes:
    if itr in range(N + 1):
        if code[0] == 'L':
            if itr != 0:
                itr -= 1
        elif code[0] == 'R':
            if itr != N:
                itr += 1
        elif code[0] == 'D':
            if itr != 0 or itr != N or itr < 0 or itr > N:
                word_lst.pop(itr)
        elif code[0] == 'P':
            word_lst.insert(itr, code[1])
            itr += 1

print("".join(word_lst))