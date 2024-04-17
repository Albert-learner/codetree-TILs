N = int(input())
n_lst = [int(input()) for _ in range(N)]


def find_carry(x, y, z):
    x_lst, y_lst, z_lst = list(map(int, str(x))), list(map(int, str(y))), list(map(int, str(z)))
    max_sum = 0

    if len(x_lst) < 5:
        for _ in range(5 - len(x_lst)):
            x_lst.insert(0, 0)
    if len(y_lst) < 5:
        for _ in range(5 - len(y_lst)):
            y_lst.insert(0, 0)
    if len(z_lst) < 5:
        for _ in range(5 - len(z_lst)):
            z_lst.insert(0, 0)

    for x_elem, y_elem, z_elem in zip(x_lst, y_lst, z_lst):
        if x_elem + y_elem + z_elem >= 10:
            return False
        else:
            max_sum = max(max_sum, x_elem + y_elem + z_elem)

    return max_sum



answer = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if find_carry(n_lst[i], n_lst[j], n_lst[k]):
                answer = n_lst[i] + n_lst[j] + n_lst[k]

print(answer)