m = int(input())
a, b = map(int, input().split())

# Please write your code here.
def steps_to_find(x, m):
    l, r = 1, m
    cnts = 0

    while True:
        mid = (l + r) // 2
        cnts += 1
        if mid == x:
            return cnts
        elif mid > x:
            r = mid - 1
        else:
            l = mid + 1

min_steps = 10 ** 18
max_steps = 0

for x in range(a, b + 1):
    s = steps_to_find(x, m)
    if s < min_steps:
        min_steps = s
    
    if s > max_steps:
        max_steps = s

print(min_steps, max_steps)