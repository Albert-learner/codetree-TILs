nums = list(map(int, input().split()))

overs, lowers = [], []
for num in nums:
    if num < 500:
        lowers.append(num)
    elif num > 500:
        overs.append(num)

print(max(lowers), min(overs))