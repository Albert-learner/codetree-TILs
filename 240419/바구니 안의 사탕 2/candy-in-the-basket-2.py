N, K = map(int, input().split())
candies_info = [0] * 101
for _ in range(N):
    candies, pos = map(int, input().split())
    candies_info[pos] += candies

answer = 0
for i in range(len(candies_info)):
    max_candies = 0
    for j in range(i - K, i + K + 1):
        if 0 <= j < len(candies_info):
            max_candies += candies_info[j]

    answer = max(answer, max_candies)

print(answer)