N = int(input())

fives = []
if N == 5 or N == 10:
    fives.append(N)

idx = 1
n_lst = [N]
while len(fives) != 2:
    idx += 1
    if (N * idx) % 5 == 0:
        fives.append(N * idx) 
    n_lst.append(N * idx)

print(*n_lst)