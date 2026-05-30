n, q = map(int, input().split())
S = input()
queries = [tuple(map(int, input().split())) for _ in range(q)]

# Please write your code here.
d1 = [0] * n
l, r = 0, -1

for i in range(n):
    k = 1 if i > r else min(d1[l + r - i], r - i + 1)

    while i - k >= 0 and i + k < n and S[i - k] == S[i + k]:
        k += 1

    d1[i] = k

    if i + k - 1 > r:
        l = i - k + 1
        r = i + k - 1

d2 = [0] * n
l, r = 0, -1

for i in range(n):
    k = 0 if i > r else min(d2[l + r - i + 1], r - i + 1)

    while i - k - 1 >= 0 and i + k < n and S[i - k - 1] == S[i + k]:
        k += 1

    d2[i] = k

    if i + k - 1 > r:
        l = i - k
        r = i + k - 1

answer = []
for a, b in queries:
    left = a - 1
    right = b - 1
    length = right - left + 1

    if length % 2 == 1:
        center = (left + right) // 2
        if d1[center] >= length // 2 + 1:
            answer.append("Yes")
        else:
            answer.append("No")
    else:
        center = (left + right + 1) // 2
        if d2[center] >= length // 2:
            answer.append("Yes")
        else:
            answer.append("No")

print("\n".join(answer))