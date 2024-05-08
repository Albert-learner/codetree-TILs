N = int(input())
n_str = input()

cases = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if n_str[i] == 'C' and n_str[j] == 'O' and n_str[k] == 'W':
                cases += 1

print(cases)