N = int(input())
B = [int(input()) for _ in range(N)]

# Please write your code here.
used = [False] * (2 * N + 1)
for b in B:
    used[b] = True

A = [i for i in range(1, 2 * N + 1) if not used[i]]

A.sort()
B.sort()

i = 0
max_scores = 0
for b in B:
    while i < N and A[i] < b:
        i += 1
    if i < N:
        max_scores += 1
        i += 1
    else:
        break

print(max_scores)