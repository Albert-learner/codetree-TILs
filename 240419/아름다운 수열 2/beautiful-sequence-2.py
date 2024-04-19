N, M = map(int, input().split())
a_seq = list(map(int, input().split()))
b_seq = list(map(int, input().split()))

answer = 0
for i in range(N - M + 1):
    check = True
    find = b_seq[:]
    for j in range(M):
        if a_seq[i + j] in find:
            find.pop(find.index(a_seq[i + j]))
        else:
            check = False
            break

    if check:
        answer += 1

print(answer)