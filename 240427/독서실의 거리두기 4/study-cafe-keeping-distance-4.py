N = int(input())
seats = list(input())

def get_dist():
    min_num = 21e8
    last_flag, cur_flag = -1, -1
    for i in range(N):
        cur_chr = seats[i]
        if cur_chr == '1':
            cur_flag = i
        else:
            cur_flag = -1
        
        if cur_flag != -1:
            if last_flag != -1:
                sub = cur_flag - last_flag
                min_num = min(min_num, sub)
            last_flag = cur_flag

    return min_num

max_dist = 0
for i in range(N):
    for j in range(i + 1, N):
        if seats[i] == '1' or seats[j] == '1':
            continue

        seats[i], seats[j] = '1', '1'
        max_dist = max(max_dist, get_dist())
        seats[i], seats[j] = '0', '0'

print(max_dist)

# # 모범답안
# n = int(input())
# seat = list(input())


# def min_dist():
#     dist = n
#     # 둘 다 1인 곳에 대해
#     # 모든 쌍을 조사하여, 그 중 가장 가까운 거리를 구합니다.
#     for i in range(n):
#         for j in range(i + 1, n):
#             if seat[i] == '1' and seat[j] == '1':
#                 dist = min(dist, j - i)
    
#     return dist


# ans = 0
# # 들어갈 위치를 일일이 정해보며
# # 그 상황에서 가장 가까운 사람간의 거리를 구해
# # 가능한 경우 중 최댓값을 계산합니다.
# for i in range(n):
#     for j in range(i + 1, n):
#         if seat[i] == '0' and seat[j] == '0':
#             # 비어있는 위치에 인원을 배치합니다.
#             seat[i] = seat[j] = '1'
#             # 가장 가까운 사람간의 거리를 구해 최댓값을 갱신해줍니다.
#             ans = max(ans, min_dist())
#             # 다시 채워졌던 값을 되돌려줍니다.
#             seat[i] = seat[j] = '0'

# print(ans)