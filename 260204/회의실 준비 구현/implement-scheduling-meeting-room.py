n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
meetings.sort(lambda x: (x[1], x[0]))

cnts = 0
last_end = -1

for s, e in meetings:
    if s >= last_end:
        cnts += 1
        last_end = e

print(cnts)
