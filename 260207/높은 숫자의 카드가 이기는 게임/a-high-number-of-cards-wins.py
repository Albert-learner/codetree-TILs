N = int(input())
B = [int(input()) for _ in range(N)]

# Please write your code here.
A = [n for n in range(1, N * 2 + 1) if n not in B]

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