N, L = map(int, input().split())
seqs = list(map(int, input().split()))

for H in range(N, -1, -1):
    l_cnt, h_cnt = 0, 0
    for i in range(N):
        if seqs[i] >= H:
            h_cnt += 1
        elif seqs[i] == H - 1:
            h_cnt += 1
            l_cnt += 1

    if h_cnt >= H and (l_cnt - (h_cnt - H)) <= L:
        print(H)
        break