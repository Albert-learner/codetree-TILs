N = int(input())

divisors = []
for i in range(1, int(N ** 0.5) + 1):
    if N % i == 0:
        divisors.append(i)
        if i != N // i and N // i != N:
            divisors.append(N // i)

if sum(divisors) == N:
    print('P')
else:
    print('N')