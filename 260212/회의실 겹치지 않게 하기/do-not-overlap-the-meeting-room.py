n = int(input())
meetings = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
meetings.sort(lambda x: (x[1], x[0]))

max_cnts, last_end = 0, -1

for start, end in meetings:
    if start >= last_end:
        max_cnts += 1
        last_end = end

print(len(meetings) - max_cnts)