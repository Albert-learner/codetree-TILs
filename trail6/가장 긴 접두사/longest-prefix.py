T = input().strip()

# Please write your code here.
R = T[::-1]

n = len(T)
pi = [0] * n

j = 0
for i in range(1, n):
    while j > 0 and T[i] != T[j]:
        j = pi[j - 1]

    if T[i] == T[j]:
        j += 1
        pi[i] = j

answer = 0
j = 0
for ch in R:
    while j > 0 and ch != T[j]:
        j = pi[j - 1]

    if ch == T[j]:
        j += 1
        answer = max(answer, j)

        if j == n:
            break

print(answer)