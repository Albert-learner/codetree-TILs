N = int(input())
people = list(map(int, input().split()))

moves = []
for i in range(N):
    move = 0
    diff_lst = [abs(j - i) for j in range(N)]

    for cst, diff in zip(people, diff_lst):
        move += cst * diff

    moves.append(move)

print(min(moves))