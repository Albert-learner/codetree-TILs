N = int(input())
n_lst = [int(input()) for _ in range(N)]

def find_carry(x, y, z):
    while x > 0 or y > 0 or z > 0:
        if (x % 10 + y % 10 + z % 10) > 9:
            return False

        x //= 10
        y //= 10
        z //= 10

    return True

answer = -1
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if find_carry(n_lst[i], n_lst[j], n_lst[k]):
                answer = max(answer, n_lst[i] + n_lst[j] + n_lst[k])

print(answer)