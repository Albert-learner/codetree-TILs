developers = list(map(int, input().split()))

def get_diff(i, j, k, w):
    sum1 = developers[i] + developers[j]
    sum2 = developers[k] + developers[w]
    sum3 = sum(developers) - (sum1 + sum2)

    if sum1 == sum2 or sum2 == sum3 or sum3 == sum1:
        return -1

    result = abs(sum1 - sum2)
    result = max(result, abs(sum1 - sum3))
    result = max(result, abs(sum2 - sum3))

    return result

min_cst = 1000001
flag = True
for i in range(5):
    for j in range(i + 1, 5):
        for k in range(5):
            for w in range(k + 1, 5):
                if i == k or i == w or j == k or j == w:
                    continue

                if get_diff(i, j, k, w) != -1:
                    min_cst = min(min_cst, get_diff(i, j, k, w))
                    flag = False

if flag:
    print(-1)
else:
    print(min_cst)