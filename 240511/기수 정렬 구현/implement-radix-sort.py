from collections import deque

N = int(input())
n_lst = list(map(int, input().split()))

buckets = [deque() for _ in range(10)]
max_val = max(n_lst)
que = deque(n_lst)
cur_ten = 1

while max_val >= cur_ten:
    while que:
        num = que.popleft()
        buckets[(num // cur_ten) % 10].append(num)

    for bucket in buckets:
        while bucket:
            que.append(bucket.popleft())

    cur_ten *= 10

print(*list(que))