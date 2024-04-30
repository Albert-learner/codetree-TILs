N, M, P = map(int, input().split())
messages = []
not_reads = []
for _ in range(M):
    c, u = input().split()
    messages.append(c)
    not_reads.append(int(u))

read_chk = [False] * 26
for i in range(M):
    if not_reads[P - 1] == 0:
        break

    if i >= P - 1:
        message = ord(messages[i]) - ord('A')
        read_chk[message] = True
    elif not_reads[i] == not_reads[P - 1]:
        message = ord(messages[i]) - ord('A')
        read_chk[message] = True


if not_reads[P - 1] == 0:
    print()
else:
    for i in range(N):
        if not read_chk[i]:
            print(chr(i + ord('A')), end = ' ')