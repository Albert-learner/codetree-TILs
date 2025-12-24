A = input()

# Please write your code here.
n = len(A)
right = [0] * (n + 1)
cnts = 0

for i in range(n - 2, -1, -1):
    if A[i] == ')' and A[i + 1] == ')':
        cnts += 1
    right[i] = cnts

ans = 0
for i in range(n - 1):
    if A[i] == '(' and A[i + 1] == '(':
        ans += right[i + 2]

print(ans)