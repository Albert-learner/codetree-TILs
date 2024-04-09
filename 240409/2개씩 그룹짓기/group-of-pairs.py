N = int(input())
n_lst = list(map(int, input().split()))

n_lst.sort()

pairs_sum = []
for i in range(len(n_lst) // 2):
    pair_sum = n_lst[i] + n_lst[-i - 1]
    pairs_sum.append(pair_sum)

print(max(pairs_sum))