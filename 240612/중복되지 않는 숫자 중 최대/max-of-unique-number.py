N = int(input())
n_lst = list(map(int, input().split()))

n_dict = {n: 0 for n in n_lst}
for n in n_lst:
    if n in n_dict:
        n_dict[n] += 1

uniques = []
for n, cnts in n_dict.items():
    if cnts == 1:
        uniques.append(n)

if len(uniques) == 0:
    print(-1)
else:
    print(max(uniques))