N = int(input())
n_str = input()

answer = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if n_str[i] == 'C' and n_str[j] == 'O' and n_str[k] == 'W':
                answer += 1

print(answer)