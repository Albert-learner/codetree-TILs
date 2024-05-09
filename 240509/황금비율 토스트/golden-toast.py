N, M = map(int, input().split())
word = input().strip()

word_lst = list(word)
itr = len(word_lst)

for i in range(M):
    cmd = input().split()
    if cmd[0] == 'L':
        itr = max(0, itr - 1)
    elif cmd[0] == 'R':
        itr = min(len(word_lst), itr + 1)
    elif cmd[0] == 'D':
        if itr < len(word_lst):
            del word_lst[itr]
    elif cmd[0] == 'P':
        ch = cmd[1]
        word_lst.insert(itr, ch)
        itr += 1

print("".join(word_lst))