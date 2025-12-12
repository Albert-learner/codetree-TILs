n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
INF = 10**18
dp_not = [-INF] * 4
dp_take = [-INF] * 4

dp_not[0] = 0               
dp_take[1] = arr[0]

for i in range(1, n):
    new_not = [-INF] * 4
    new_take = [-INF] * 4

    for c in range(4):
        new_not[c] = max(dp_not[c], dp_take[c])

    for c in range(1, 4):
        if dp_not[c - 1] > -INF:
            new_take[c] = dp_not[c - 1] + arr[i]
    
    dp_not, dp_take = new_not, new_take

answer = max(dp_not[3], dp_take[3])
print(answer)