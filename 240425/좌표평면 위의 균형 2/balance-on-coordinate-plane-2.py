import sys

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]
x_lst, y_lst = list(list(zip(*points))[0]), list(list(zip(*points))[1])

min_cnts = sys.maxsize
for i in range(101):
    if i % 2 == 1:
        continue

    for j in range(101):
        if j % 2 == 1:
            continue

        n1, n2, n3, n4 = 0, 0, 0, 0
        for k in range(N):
            if x_lst[k] < i and y_lst[k] > j:
                n1 += 1
            elif x_lst[k] > i and y_lst[k] > j:
                n2 += 1
            elif x_lst[k] > i and y_lst[k] < j:
                n3 += 1
            else:
                n4 += 1

        max_cnt = max(n1, n2)
        max_cnt = max(max_cnt, n3)
        max_cnt = max(max_cnt, n4)

        min_cnts = min(min_cnts, max_cnt)

print(min_cnts)