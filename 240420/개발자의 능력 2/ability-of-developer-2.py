developers = list(map(int, input().split()))
developers.sort()

result = []
for i in range(len(developers) // 2):
    result.append(developers[i] + developers[-i - 1])
result.sort()

print(result[-1] - result[0])