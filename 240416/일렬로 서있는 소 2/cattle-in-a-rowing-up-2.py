N = int(input())
cows = list(map(int, input().split()))

answer = 0
for i in range(len(cows)):
    for j in range(i + 1, len(cows)):
        for k in range(j + 1, len(cows)):
            if cows[i] <= cows[j] <= cows[k]:
                answer += 1

print(answer)