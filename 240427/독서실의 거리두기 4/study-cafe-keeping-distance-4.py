N = int(input())
seats = list(input())

max_dist = 0
for i in range(N):
    if seats[i] == '1':
        continue

    dist = float("inf")
    for j in range(N):
        if seats[j] == '1' or i == j:
            continue
        
        dist = N + 2
        seats[i], seats[j] = '1', '1'
        for k in range(N):
            for l in range(k + 1, N):
                if seats[k] == '1' and seats[l] == '0':
                    dist = min(dist, l - k + 1)

        max_dist = max(max_dist, dist)
        seats[i], seats[j] = '0', '0'

print(max_dist)