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

# # 모범답안
# MAX_T = 1000

# # 변수 선언 및 입력
# n, c, g, h = tuple(map(int, input().split()))
# ta, tb = [0] * n, [0] * n

# for i in range(n):
#     ta[i], tb[i] = tuple(map(int, input().split()))


# # 특정 장비의 t 온도에서의 작업량을 계산합니다.
# def single_efficiency(low, high, t):
#     if t < low:
#         return c
#     elif t <= high:
#         return g
#     else:
#         return h


# # 온도 t에 대한 작업량을 계산합니다.
# def performance(t):
#     total_efficiency = 0

#     # 장비별 작업량의 합을 계산합니다.
#     for i in range(n):
#         total_efficiency += single_efficiency(ta[i], tb[i], t)
#     return total_efficiency


# # 각 온도에 대해 작업량을 계산하여
# # 그 중 최댓값을 구해줍니다.
# max_out = 0
# for t in range(MAX_T + 1):
#     max_out = max(max_out, performance(t))

# print(max_out)