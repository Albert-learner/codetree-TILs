N, M = map(int, input().split())
n_lst = list(map(int, input().split()))

max_sum = 0
for move_pos in range(N):
    move_cost = [n_lst[move_pos]]
    for _ in range(M - 1):
        real_pos_cost = n_lst[move_cost[-1] - 1]
        move_cost.append(real_pos_cost)

    max_sum = max(max_sum, sum(move_cost))

print(max_sum)