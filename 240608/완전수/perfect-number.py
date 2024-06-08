start, end = map(int, input().split())

complete_nums = 0
for N in range(start, end + 1):
    n_aliquots = []
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            n_aliquots.append(i)
            if i != N // i:
                n_aliquots.append(N // i)

    n_aliquots = sorted([n_aliq for n_aliq in n_aliquots if n_aliq != N])
    if sum(n_aliquots) == N:
        complete_nums += 1

print(complete_nums)