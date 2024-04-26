N, M = map(int, input().split())
pairs = [tuple(sorted(map(int, input().split()))) for _ in range(M)]

pairs_dict = {}
for pair in pairs:
    pairs_dict[pair] = pairs_dict.get(pair, 0) + 1

print(max(pairs_dict.values()))