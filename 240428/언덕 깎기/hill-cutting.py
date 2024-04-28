N = int(input())
hills = [int(input()) for _ in range(N)]
hills.sort()

costs = 0
half_hills = len(hills) // 2
finish = False
for i in range(half_hills):
    for j in range(len(hills) - 1, 0, -1):
        if hills[j] - hills[i] > 17:
            costs += (hills[i + 1] - hills[i]) ** 2
            costs += (hills[j] - hills[j - 1]) ** 2
            hills[i] = hills[i + 1]
            hills[j] = hills[j - 1]
        else:
            finish = True
            break
    
    if finish:
        break
            
print(costs)