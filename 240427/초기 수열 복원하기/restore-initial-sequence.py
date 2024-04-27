N = int(input())
n_lst = list(map(int, input().split()))

for i in range(N):
    success = True
    originals = [0] * N
    originals[0] = i + 1
    exist = [False] * (N + 1)
    for j in range(N - 1):
        diff = n_lst[j] - originals[j]
        if diff <= 0 or diff > N:
            success = False
            break
        
        if exist[diff]:
            success = False
            break

        exist[diff] = True
        originals[j + 1] = diff

    if success:
        print(*originals)
        break