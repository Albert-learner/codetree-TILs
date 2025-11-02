n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Please write your code here.
A_set, B_set = set(A), set(B)
set_diff = A_set.symmetric_difference(B_set)

print(len(set_diff))