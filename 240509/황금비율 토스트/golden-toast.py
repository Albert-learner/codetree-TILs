N, M = map(int, input().split())
word_lst = list(input())
left, right = [], []

for _ in range(M):
    cmd = input().split()
    if cmd[0] == 'L' and word_lst:
        right.append(word_lst.pop())
    elif cmd[0] == 'D' and right:
        word_lst.append(right.pop())
    elif cmd[0] == 'P':
        word_lst.append(cmd[1])

print("".join(word_lst))