T, a, b = map(int, input().split())
S, N = [], []
poses = [0] * b
for _ in range(T):
    alphabet, pos = input().split()
    
    if alphabet == 'S':
        S.append(int(pos))
    elif alphabet == 'N':
        N.append(int(pos))

S.sort()
N.sort()
s_idx, n_idx, nearest_cnts = 0, 0, 0

for cur_pos in range(a, b + 1):
    while s_idx < len(S) - 1 and abs(cur_pos - S[s_idx]) > abs(cur_pos - S[s_idx + 1]):
        s_idx += 1

    s_dst = abs(cur_pos - S[s_idx])
    
    while n_idx < len(N) - 1 and abs(cur_pos - N[n_idx]) > abs(cur_pos - N[n_idx + 1]):
        n_idx += 1
    
    n_dst = abs(cur_pos - N[n_idx])

    if s_dst <= n_dst:
        nearest_cnts += 1

print(nearest_cnts)