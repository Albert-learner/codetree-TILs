n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
best = cur = arr[0]
for x in arr[1:]:
    cur = max(x, cur + x)  
    best = max(best, cur)

print(best)