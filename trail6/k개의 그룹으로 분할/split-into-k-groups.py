n, k = map(int, input().split())
a = list(map(int, input().split()))

# Please write your code here.
total = sum(a)

if total % k != 0:
    print("No")
else:
    target = total // k

    if max(a) > target:
        print("No")
    else:
        size = 1 << n
        dp = [-1] * size
        dp[0] = 0

        for mask in range(size):
            if dp[mask] == -1:
                continue

            for i in range(n):
                if mask & (1 << i):
                    continue

                next_sum = dp[mask] + a[i]

                if next_sum > target:
                    continue

                next_mask = mask | (1 << i)

                next_value = next_sum % target

                if dp[next_mask] == -1:
                    dp[next_mask] = next_value

        if dp[size - 1] == 0:
            print("Yes")
        else:
            print("No")