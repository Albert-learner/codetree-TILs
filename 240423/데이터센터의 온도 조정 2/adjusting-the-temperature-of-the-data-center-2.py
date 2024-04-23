N, C, G, H = map(int, input().split())
degrees = [tuple(map(int, input().split())) for _ in range(N)]
Ta, Tb = list(list(zip(*degrees))[0]), list(list(zip(*degrees))[1])

max_time = 1000
max_works = 0
def get_works(l, h, t):
    if t < l:
        return C
    elif l <= t <= h:
        return G
    else:
        return H

def get_degrees(t):
    total = 0
    for ta, tb in zip(Ta, Tb):
        total += get_works(ta, tb, t)

    return total

for time in range(max_time + 1):
    max_works = max(max_works, get_degrees(time))

print(max_works)