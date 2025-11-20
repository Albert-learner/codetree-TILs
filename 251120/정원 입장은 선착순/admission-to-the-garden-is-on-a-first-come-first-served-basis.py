N = int(input())
a, t = [], []
for _ in range(N):
    ai, ti = map(int, input().split())
    a.append(ai)
    t.append(ti)

# Please write your code here.
import heapq

people = [(a[i], i) for i in range(N)]
people.sort()

cur_time = 0          
idx = 0                   
waiting = []              
max_wait = 0              
processed = 0             

while processed < N:
    if not waiting:
        arrival_time, person_idx = people[idx]
        cur_time = max(cur_time, arrival_time)

        while idx < N and people[idx][0] <= cur_time:
            _, p_idx = people[idx]
            heapq.heappush(waiting, p_idx)
            idx += 1

    p = heapq.heappop(waiting)
    wait_time = cur_time - a[p]
    if wait_time > max_wait:
        max_wait = wait_time

    cur_time += t[p]
    processed += 1

    while idx < N and people[idx][0] <= cur_time:
        _, p_idx = people[idx]
        heapq.heappush(waiting, p_idx)
        idx += 1

print(max_wait)