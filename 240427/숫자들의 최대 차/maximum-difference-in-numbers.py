N, K = map(int, input().split())
n_lst = [int(input()) for _ in range(N)]
n_lst.sort()

max_cnts = 0
for i in range(N):
    cnts = 1
    for j in range(i + 1, N):
        if abs(n_lst[j] - n_lst[i]) <= K:
            cnts += 1
        else:
            break

    max_cnts = max(max_cnts, cnts)

print(max_cnts)