n = int(input())
group = []
group_size = []

for _ in range(n):
    nums = list(map(int, input().split()))
    group_size.append(nums[0])
    group.append(nums[1:])

# Please write your code here.
MOD = 10007

person_groups = [0] * 101

for group_idx in range(n):
    for person in group[group_idx]:
        person_groups[person] |= 1 << group_idx

dp = [0] * (1 << n)
dp[0] = 1

for person in range(1, 101):
    next_dp = dp[:] 

    available_groups = person_groups[person]

    for mask in range(1 << n):
        if dp[mask] == 0:
            continue

        candidates = available_groups & ~mask

        while candidates:
            bit = candidates & -candidates
            new_mask = mask | bit

            next_dp[new_mask] += dp[mask]
            next_dp[new_mask] %= MOD

            candidates -= bit

    dp = next_dp

print(dp[(1 << n) - 1])