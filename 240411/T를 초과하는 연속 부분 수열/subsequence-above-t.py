N, T = map(int, input().split())
n_lst = list(map(int, input().split()))

answer, cnts, num = 0, 0, 0
for i in range(N):
    n_new = n_lst[i]
    if n_new > T:
        cnts += 1
    else:
        cnts = 0

    answer = max(answer, cnts)
    num = n_new

print(answer)