N = int(input())
coords = [tuple(map(int, input().split())) for _ in range(N)]

x_lst, y_lst = list(list(zip(*coords))[0]), list(list(zip(*coords))[1])
dsts = []
for i in range(N):
    tmp_x_lst = x_lst.copy()
    tmp_y_lst = y_lst.copy()
    del tmp_x_lst[i]
    del tmp_y_lst[i]

    dsts.append((max(tmp_x_lst) - min(tmp_x_lst) ** 2 + (max(tmp_y_lst) - min(tmp_y_lst) ** 2)))

print(min(dsts))