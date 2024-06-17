N, T = map(int, input().split())
belt = [list(map(int, input().split())) for _ in range(2)]
it_first_col = 0

while T > 0:
    tmp = belt[0][(it_first_col + (N - 1)) % N]
    belt[0][(it_first_col + (N - 1)) % N] = belt[1][(it_first_col + (N - 1)) % N]
    belt[1][(it_first_col + (N - 1)) % N] = tmp

    it_first_col = (it_first_col - 1 + N) % N
    T -= 1

for ir in range(2):
    for ic in range(it_first_col, it_first_col + N):
        print(belt[ir][ic % N], end = ' ')
    print()