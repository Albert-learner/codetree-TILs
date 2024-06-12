n1, n2 = map(int, input().split())
a_lst = list(map(int, input().split()))
b_lst = list(map(int, input().split()))

if n1 < n2:
    a_lst, b_lst = b_lst, a_lst

check = False
for i in range(n1 - n2 + 1):
    if a_lst[i: i + n2] == b_lst:
        check = True
        break

print("Yes" if check == True else "No")