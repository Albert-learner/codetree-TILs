import sys

N = int(input())
n_lst = list(map(int, input().split()))

min_sum = sys.maxsize
for i in range(N):
    n_lst[i] *= 2

    for j in range(N):
        process_n_lst = []
        for k in range(N):
            if j != k:
                process_n_lst.append(n_lst[k])

        process_sum = 0
        for k in range(N - 2):
            process_sum += abs(process_n_lst[k + 1] - process_n_lst[k])

        min_sum = min(min_sum, process_sum)
        
    n_lst[i] //= 2
    
print(min_sum)