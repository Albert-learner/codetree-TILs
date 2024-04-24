N = int(input())
n_lst = sorted(list(map(int, input().split())))

max_cnts = 0
for num in range(1, 101):
    cnts = 0
    for i in range(N):
        for j in range(i, N):
            if (n_lst[i] + n_lst[j]) / 2 == num:
                cnts += 1

    max_cnts = max(max_cnts, cnts)

print(max_cnts)