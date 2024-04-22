N, M, D, S = map(int, input().split())

class EatCheezes:
    def __init__(self, p, m, t):
        self.p, self.m, self.t = p, m, t

class AcheTimes:
    def __init__(self, p, t):
        self.p, self.t = p, t

eat_cheezes = [EatCheezes(*tuple(map(int, input().split()))) for _ in range(D)]
ache_times = [AcheTimes(*tuple(map(int, input().split()))) for _ in range(S)]

max_medicines = 0
for i in range(1, M + 1):
    time = [0] * (N + 1)
    for eat_cheeze in eat_cheezes:
        if eat_cheeze.m != i:
            continue

        person = eat_cheeze.p
        if time[person] == 0 or time[person] > eat_cheeze.t:
            time[person] = eat_cheeze.t

    possible = True
    for ache_time in ache_times:
        person = ache_time.p
        if time[person] == 0 or time[person] >= ache_time.t:
            possible = False

    medicines = 0
    if possible:
        for j in range(1, N + 1):
            if time[j] != 0:
                medicines += 1

        max_medicines = max(max_medicines, medicines)

print(max_medicines)