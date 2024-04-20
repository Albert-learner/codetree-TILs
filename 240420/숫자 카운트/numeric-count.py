N = int(input())
B_asks = []
for _ in range(N):
    num, cnt1, cnt2 = map(int, input().split())
    num = list(map(int, str(num)))
    B_asks.append([num[0], num[1], num[2], cnt1, cnt2])

cnts = 0
for i in range(1, 10):
    for j in range(1, 10):
        for k in range(1, 10):
            if i == j or j == k or k == i:
                continue

            b_pred = [i, j, k]
            satisfied = True
            for b_ask in B_asks:
                cnt1, cnt2 = 0, 0

                for l in range(3):
                    for n in range(3):
                        if b_pred[l] == b_ask[n]:
                            if l == n:
                                cnt1 += 1
                            else:
                                cnt2 += 1

                if cnt1 != b_ask[3] or cnt2 != b_ask[4]:
                    satisfied = False

            if satisfied:
                cnts += 1

print(cnts)