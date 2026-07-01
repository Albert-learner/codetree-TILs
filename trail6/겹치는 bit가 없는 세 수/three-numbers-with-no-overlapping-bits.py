# 변수 선언 및 입력:
n = int(input())
arr = list(map(int, input().split()))

# 모든 숫자에 대해 겹치지 않는 쌍을 찾습니다.
# 맞을 경우 합을 더해줍니다.
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        for k in range(j + 1, n):
            # 숫자들의 비트가 겹치지 않는다면
            # 세 숫자의 합과, 세 숫자의 or연산의 값이 같습니다.
            if arr[i] + arr[j] + arr[k] == (arr[i] | arr[j] | arr[k]):
                ans = max(ans, arr[i] + arr[j] + arr[k])

# 조건을 만족하는 경우 중 얻을 수 있는 최대 합을 출력합니다.
print(ans)
