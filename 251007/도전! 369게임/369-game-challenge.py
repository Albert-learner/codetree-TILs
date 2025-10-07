n = input()

# Please write your code here.
int_n = int(n)
n_lst = [i for i in range(1, int_n + 1)]
n_str_lst = [str(i) for i in range(1, int_n + 1)]

MOD = 10 ** 9 + 7
claps = 0
for n, n_str in zip(n_lst, n_str_lst):
    if n % 3 == 0 or any(ch in n_str for ch in ['3', '6', '9']):
        claps += 1

print(claps % MOD)