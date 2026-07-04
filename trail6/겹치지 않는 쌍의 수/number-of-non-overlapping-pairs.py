n = int(input())

arr = [0 for _ in range(n)]

# 각 그룹의 정보를 입력받습니다.
for i in range(n):
    infos = map(int, input().split()[1:])
    for info in infos:
        # 각 그룹의 정보를 비트로 관리합니다.
        # x번 사람이 있을 경우
        # (1 << x)에 해당하는 비트가 1이 됩니다.
        arr[i] |= (1 << info)

# 모든 그룹에 대해 겹치지 않는 모든 쌍의 개수를 찾습니다.
ans = 0
for i in range(n):
    for j in range(i + 1, n):
        # 두 그룹에 속한 사람 번호가 겹치지 않는다는 뜻은
        # 두 그룹을 and연산했을 때 0이 됨을 의미합니다.
        if (arr[i] & arr[j]) == 0:
            ans += 1

# 조건을 만족하는 그룹의 순서쌍의 개수를 출력합니다.
print(ans)
