n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
j = 0
for x in A:
    if j < m and x == B[j]:
        j += 1
        if j == m:
            break

print("Yes" if j == m else "No")