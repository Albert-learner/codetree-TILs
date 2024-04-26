N = int(input())
n_str = input()

pattern_cnts = {}
for s_len in range(1, N):
    for chr_idx in range(N - s_len + 1):
        if n_str[chr_idx:chr_idx + s_len] not in pattern_cnts:
            pattern_cnts[n_str[chr_idx:chr_idx + s_len]] = 1
        else:
            pattern_cnts[n_str[chr_idx:chr_idx + s_len]] += 1

patterns = []
max_length = max(map(len, pattern_cnts.keys()))

for length in range(1, max_length + 1):
    tmp = []
    for pattern, cnts in pattern_cnts.items():
        if len(pattern) == length:
            tmp.append((pattern, cnts))

    if tmp:
        patterns.append(tmp)

min_length = 0
patterns_sort = sorted(patterns, key = lambda x: x[0][1], reverse=True)
for pattern_lst in patterns_sort:
    patterns, pattern_cnts = list(zip(*pattern_lst))[0], list(zip(*pattern_lst))[1]
    if 2 in pattern_cnts:
        continue
    else:
        min_length = len(patterns[0])
        break

print(min_length)