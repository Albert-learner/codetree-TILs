n_str, a_str = input().split()
N = int(n_str)
str_lst = [input() for _ in range(N)]

same_cnts = 0
for e_str in str_lst:
    if e_str == a_str:
        same_cnts += 1

print(same_cnts)