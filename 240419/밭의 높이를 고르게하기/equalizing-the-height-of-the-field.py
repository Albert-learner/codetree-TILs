N, H, T = map(int, input().split())
heights = list(map(int, input().split()))
test_heights = heights[:]

cost = 0
min_cost = 100000
for i in range(N):
    if (i + T) <= N:
        for j in range(i, i + T):
            if heights[j] < H:
                while heights[j] != H:
                    heights[j] += 1
                    cost += 1
            elif heights[j] > H:
                while heights[j] != H:
                    heights[j] -= 1
                    cost += 1
        
        min_cost = min(min_cost, cost)
    
    cost = 0
    heights = test_heights[:]

print(min_cost)