n = int(input())
dist = list(map(int, input().split()))
cost = list(map(int, input().split()))

# Please write your code here.
min_cost = cost[0]
answer = 0

for i in range(n - 1):
    if cost[i] < min_cost:
        min_cost = cost[i]
    answer += min_cost * dist[i]

print(answer)