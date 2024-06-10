first, second = map(int, input().split())

fibs_lst = [first, second]
while len(fibs_lst) != 10:
    fibs_lst.append((fibs_lst[-1] + fibs_lst[-2]) % 10)

print(*fibs_lst)