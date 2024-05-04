N, M = map(int, input().split())
people = list(map(int, input().split()))

if M == 0:
    print(N - 1)
elif 0 < M and M * 2 + 1 < N:
    print(N // (M * 2 + 1))
elif N < M * 2 + 1:
    print((M * 2 + 1) // N)