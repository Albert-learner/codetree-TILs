N, M = map(int, input().split())
people = list(map(int, input().split()))

if M == 0:
    print(N - 1)
else:
    print(N // (M * 2 + 1))