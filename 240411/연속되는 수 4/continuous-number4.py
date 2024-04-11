N = int(input())

answer, cnts, num = 0, 0, 0
for i in range(N):
    n_new = int(input())
    if n_new > num:
        cnts += 1
    else:
        cnts = 1

    answer = max(cnts, answer)
    num = n_new

print(answer)