start, end = map(int, input().split())

three_aliquots = 0
for N in range(start, end + 1):
    n_aliquots = []
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            n_aliquots.append(i)
            if i != N // i:
                n_aliquots.append(N // i)

    n_aliquots.sort()
    if len(n_aliquots) == 3:
        three_aliquots += 1

print(three_aliquots)