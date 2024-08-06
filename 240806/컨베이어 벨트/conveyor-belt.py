# My Solution
N, T = map(int, input().split())
belt = [list(map(int, input().split())) if r_idx % 2 == 0 else list(map(int, input().split()))[::-1]
        for r_idx in range(2)]

while T > 0:
    right_top, left_bottom = belt[0][N - 1], belt[1][0]
    for r_idx in range(len(belt)):
        if r_idx % 2 == 0:
            belt[r_idx] = [left_bottom] + belt[r_idx][:-1]
        else:
            belt[r_idx] = belt[r_idx][1:] + [right_top]
    T -= 1

for r_idx, row in enumerate(belt):
    if r_idx % 2 == 0:
        print(*row)
    else:
        print(*row[::-1])

# N, T = map(int, input().split())
# belt = [list(map(int, input().split())) for _ in range(2)]
# it_first_col = 0

# while T > 0:
#     tmp = belt[0][(it_first_col + (N - 1)) % N]
#     belt[0][(it_first_col + (N - 1)) % N] = belt[1][(it_first_col + (N - 1)) % N]
#     belt[1][(it_first_col + (N - 1)) % N] = tmp

#     it_first_col = (it_first_col - 1 + N) % N
#     T -= 1

# for ir in range(2):
#     for ic in range(it_first_col, it_first_col + N):
#         print(belt[ir][ic % N], end = ' ')
#     print()