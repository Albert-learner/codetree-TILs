n, k = map(int, input().split())
a = list(map(int, input().split()))

total = sum(a)

# 전체 합이 K로 나누어 떨어지지 않으면 불가
if total % k != 0:
    print("No")
else:
    target = total // k

    # 각 부분집합의 합 미리 계산
    subset_sum = [0] * (1 << n)
    for mask in range(1 << n):
        for i in range(n):
            if (mask >> i) & 1:
                subset_sum[mask] += a[i]

    # dp[mask]: mask에 해당하는 원소들을 
    #           target씩 그룹으로 완전히 나눌 수 있으면 True
    dp = [False] * (1 << n)
    dp[0] = True  # 빈 집합은 분할 완료

    for mask in range(1 << n):
        if not dp[mask]:
            continue

        # mask에서 아직 사용되지 않은 원소들
        remaining = ((1 << n) - 1) ^ mask  # 전체 XOR mask

        # remaining의 부분집합 중 합이 target인 것 탐색
        sub = remaining
        while sub > 0:
            if subset_sum[sub] == target:
                dp[mask | sub] = True
            sub = (sub - 1) & remaining  # 다음 부분집합

    print("Yes" if dp[(1 << n) - 1] else "No")