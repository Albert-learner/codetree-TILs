# 변수 선언 및 입력:
n, k = tuple(map(int, input().split()))
arr = [0] + [
    int(input())
    for _ in range(n)
]

# two pointer를 적용하기 위해
# 먼저 주어진 숫자들을 정렬해줍니다.
arr.sort()

# 2개의 원소 합이 k 이하인
# 서로 다른 가짓수를 구해줍니다.
ans = 0

# 숫자 i에 대해
# arr[i] + arr[j] <= k를 만족하는 j중
# 최대의 j가 잡히도록
# two pointer를 진행합니다.
j = n
for i in range(1, n + 1):
    # 구간 내 합이 k보다 크면 계속 진행합니다.
    while j != 1 and arr[i] + arr[j] > k:
        j -= 1

    # j가 i보다 같거나 작아져야만 두 숫자의 합이 k 이내가 된다면
    # 더 이상 진행이 의미가 없으므로 종료합니다.
    if j <= i:
        break

    # 현재 숫자 arr[i]에 대해
    # [i + 1, j] 내에 있는 모든 숫자가 정확히
    # arr[i]와의 합이 k 이하가 되는 경우임을
    # 확신할 수 있으므로 j - i를 답에 더해줍니다.
    ans += j - i

print(ans)
