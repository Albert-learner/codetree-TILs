N, M = map(int, input().split())
bulkheads = list(map(int, input().split()))

for i in range(max(bulkheads), sum(bulkheads) + 1):
    tmp = []
    total = bulkheads[0]
    for j in range(1, N):
        if total + bulkheads[j] > i:
            tmp.append(total)
            total = bulkheads[j]
        else:
            total += bulkheads[j]

    tmp.append(total)
    if len(tmp) <= M:
        print(i)
        break