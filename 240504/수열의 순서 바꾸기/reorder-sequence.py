N = int(input())
n_lst = list(map(int, input().split()))

cnts = 0
for i in range(N):
    flag = False
    for j in range(i, N - 1):
        if n_lst[j] > n_lst[j + 1]:
            flag = True

    if flag:
        cnts += 1

print(cnts)