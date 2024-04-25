from collections import Counter

N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]
x_lst, y_lst = list(list(zip(*points))[0]), list(list(zip(*points))[1])

cntr_x = Counter(x_lst)
cntr_y = Counter(y_lst)

answer = 0
lines = 0
for x, x_cnt in cntr_x.items():
    if x_cnt >= 2:
        lines += 1

for y, y_cnt in cntr_y.items():
    if y_cnt >= 2:
        lines += 1

answer = 1 if lines == 3 else 0
print(answer)