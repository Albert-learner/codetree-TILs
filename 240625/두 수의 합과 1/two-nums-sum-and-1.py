first, second = map(int, input().split())

total = first + second
one_cnts = 0

for n_str in str(total):
    if n_str == '1':
        one_cnts += 1

print(one_cnts)