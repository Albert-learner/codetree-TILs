N = int(input())
n_lst = list(map(int, input().split()))

moves = []
for i in range(N):
    diff_lst = [abs(j - i) for j in range(N)]

    move = 0
    for n, diff in zip(n_lst, diff_lst):
        move += n * diff

    moves.append(move)
    
print(min(moves))