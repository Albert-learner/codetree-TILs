N = int(input())
heights = list(map(int, input().split()))

answer = 0
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            if heights[i] <= heights[j] and heights[j] <= heights[k] and heights[i] <= heights[k]:
                answer += 1

print(answer)