n = int(input())
k = int(input())

# Please write your code here.
A = [[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]
A_lst = sorted(sum(A, []))

print(A_lst[k - 1])