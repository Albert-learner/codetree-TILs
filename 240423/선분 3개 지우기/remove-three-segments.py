N = int(input())
lines = [tuple(map(int, input().split())) for _ in range(N)]

cases = 0
total_lines = set(lines)
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            
            confirm_lines = [0] * 100
            flag = True

            for l in range(N):
                if l == i or l == j or l == k:
                    continue

                for m in range(lines[l][0], lines[l][1] + 1):
                    confirm_lines[m] += 1
                    if confirm_lines[m] > 1:
                        flag = False

            if flag:
                cases += 1

print(cases)