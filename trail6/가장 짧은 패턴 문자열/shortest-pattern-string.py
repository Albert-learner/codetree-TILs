T = input().strip()

# Please write your code here.
n = len(T)

pi = [0] * n

j = 0
for i in range(1, n):
    while j > 0 and T[i] != T[j]:
        j = pi[j - 1]

    if T[i] == T[j]:
        j += 1
        pi[i] = j

print(n - pi[-1])