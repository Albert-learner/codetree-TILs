N = int(input())
n_lst = list(map(int, input().split()))

answer = 0
for i in range(N):
    for j in range(i + 1, N):
        areas = n_lst[i:j + 1]
        if sum(areas) // len(areas) in areas:
            answer += 1

print(answer)