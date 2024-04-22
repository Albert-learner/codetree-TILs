N, M, D, S = map(int, input().split())
eat_cheezes = [[] for _ in range(N)]
for _ in range(D):
    p, m, t = map(int, input().split())
    eat_cheezes[p - 1].append([m, t])

for i in range(N):
    eat_cheezes[i].sort(key = lambda x: x[-1])

ache_times = sorted([tuple(map(int, input().split())) for _ in range(S)], key = lambda x: x[-1])

answer = set()
cnts = [0] * (M + 1)
for ache_person, ache_time in ache_times:
    cheezes = set()
    for eat_cheeze_num, eat_time in eat_cheezes[ache_person - 1]:
        if eat_time >= ache_time:
            break

        cheezes.add(eat_cheeze_num)
    
    for eat_cheeze in cheezes:
        cnts[eat_cheeze] += 1

for i in range(1, M + 1):
    if cnts[i] == S:
        answer.add(i)

max_medicines = 0
for eat_cheeze in eat_cheezes:
    found = False
    for cheeze_num, eat_time in eat_cheeze:
        if cheeze_num in answer:
            found = True
            break
    
    if found:
        max_medicines += 1

print(max_medicines)