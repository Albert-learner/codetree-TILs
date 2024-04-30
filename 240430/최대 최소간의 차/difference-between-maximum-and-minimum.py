import sys

N, K = map(int, input().split())
MAX_N, MAX_K = 100, 10000
n_lst = list(map(int, input().split()))

for _ in range(MAX_N - len(n_lst)):
    n_lst.append(0)

cst = 0
while True:
    cur_min, cur_max = MAX_K, 1
    min_idx, max_idx = 0, 0
    for i in range(N):
        if cur_min > n_lst[i]:
            cur_min = n_lst[i]
            min_idx = i
        if cur_max < n_lst[i]:
            cur_max = n_lst[i]
            max_idx = i

    min_cnts = n_lst.count(cur_min)
    max_cnts = n_lst.count(cur_max)

    if cur_max - cur_min <= K:
        break
    else:
        if min_cnts >= max_cnts:
            n_lst[max_idx] -= 1
            cst += 1
        else:
            n_lst[min_idx] += 1
            cst += 1

print(cst)

# # 모범답안
# import sys

# INT_MAX = sys.maxsize
# MAX_K = 10000

# # 변수 선언 및 입력:
# n, k = tuple(map(int, input().split()))
# arr = list(map(int, input().split()))


# def get_cost(low, high):
#     cost = 0
#     # 각 수에 대해 low ~ high 사이로 바꾸는데 드는 cost를 계산해 줍니다.
#     for elem in arr:
#         # low보다 작은 경우 low로 만들어 주는 게 최소 cost입니다.
#         if elem < low: 
#             cost += low - elem
#         # high보다 큰 경우 high로 만들어 주는게 최소 cost입니다.
#         if elem > high: 
#             cost += elem - high
#         # 그 외의 경우 이미 구간 안에 있기 때문에 cost가 필요하지 않습니다.

#     return cost

   
# ans = INT_MAX
# # 모든 구간 쌍 (num, num + k)를 잡아보며
# # 그 구간으로 만들기 위한 비용을 계산하여
# # 그 중 최솟값을 계산합니다.
# for num in range(1, MAX_K + 1):
#     ans = min(ans, get_cost(num, num + k))

# print(ans)