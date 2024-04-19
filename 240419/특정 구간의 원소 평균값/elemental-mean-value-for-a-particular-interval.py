N = int(input())
n_lst = list(map(int, input().split()))

exist = False
answer = 0
for i in range(N):
    for j in range(i, N):
        sum_val = 0
        for k in range(i, j + 1):
            sum_val += n_lst[k]
        

        avg = sum_val / (j - i + 1)
        for k in range(i, j + 1):
            if n_lst[k] == avg:
                exist = True

        if exist:
            answer += 1
            exist = False

print(answer)