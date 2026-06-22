n, m = map(int, input().split())
cards = [0] + list(map(int, input().split()))

# Please write your code here.
INF = 10 ** 18

dp = {(0, 0, 0): 0}

for i in range(1, n + 1):
    new_dp = {}

    for (last1, last2, discarded), cost in dp.items():
        add = 0 if last1 == 0 else abs(cards[i] - cards[last1])
        state = (i, last2, discarded)
        new_dp[state] = min(new_dp.get(state, INF), cost + add)

        add = 0 if last2 == 0 else abs(cards[i] - cards[last2])
        state = (last1, i, discarded)
        new_dp[state] = min(new_dp.get(state, INF), cost + add)

        if discarded < m:
            state = (last1, last2, discarded + 1)
            new_dp[state] = min(new_dp.get(state, INF), cost)

    dp = new_dp

print(min(dp.values()))