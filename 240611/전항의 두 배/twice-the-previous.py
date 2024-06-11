a1, a2 = map(int, input().split())

a_lst = [a1, a2]
while len(a_lst) < 10:
    a_lst.append(a_lst[-1] + 2 * a_lst[-2])

print(*a_lst)