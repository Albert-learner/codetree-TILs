abilities = list(map(int, input().split()))

def get_diff(i, j):
    sum1 = abilities[i] + abilities[j]
    sum2 = sum(abilities) - sum1

    return abs(sum1 - sum2)

min_diff = 1000001
for i in range(0, len(abilities)):
    for j in range(i + 1, len(abilities)):
        min_diff = min(min_diff, get_diff(i, j))

print(min_diff)