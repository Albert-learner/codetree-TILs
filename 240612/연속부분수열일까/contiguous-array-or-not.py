n1, n2 = map(int, input().split())
a_lst = list(map(int, input().split()))
b_lst = list(map(int, input().split()))

print("Yes" if b_lst in a_lst else "No")