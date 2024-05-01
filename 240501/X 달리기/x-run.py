X = int(input())

cur_pos, cur_speed = 0, 1
total_times = 0

while True:
    cur_pos += cur_speed
    total_times += 1
    cur_speed += 1
    gradients = 0

    if cur_pos == X:
        break

    for i in range(cur_speed):
        gradients += i
    
    if X - (cur_pos + cur_speed) < gradients:
        cur_speed -= 1

    stays = 0
    for i in range(cur_speed):
        stays += i
    if X - (cur_pos + cur_speed) < stays:
        cur_speed -= 1

print(total_times)

# # 모범답안
# # 변수 선언 및 입력
# x = int(input())
# t = 0
# left_dist = x
# v = 1

# while True:
#     left_dist -= v
#     t += 1

#     if left_dist == 0:
#         break

#     # 속도를 더 높여도 괜찮은지 결정합니다.
#     # 속도를 1 더 높이면, (v + 1) + v + (v - 1) + ... + 2 + 1 만큼 이동하게 됩니다.
#     # 즉, 남은 거리가 (v + 1) * (v + 2) / 2 보다 크거나 같아야 합니다.
#     if left_dist >= (v + 1) * (v + 2) / 2:
#         v += 1
    
#     # 속도를 유지해도 괜찮은지 결정합니다.
#     # 속도를 유지하면, v + (v - 1) + ... + 2 + 1 만큼 이동하게 됩니다.
#     # 즉, 남은 거리가 v * (v + 1) / 2 보다 크거나 같아야 합니다.
#     elif left_dist >= v * (v + 1) / 2:
#         # 아무 것도 하지 않습니다.
#         pass

#     # 위 둘을 만족하지 못하면 반드시 속도를 줄여야만 합니다.
#     else:
#         v -= 1

# print(t)