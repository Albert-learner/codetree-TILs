N = int(input())
birds = sorted([tuple(map(int, input().split())) for _ in range(N)], key = lambda x: x[0])

cnts = 0
cur_bird = birds[0]
for i in range(1, N):
    if birds[i][0] != cur_bird[0]:
        cur_bird = birds[i]
    else:
        if birds[i][1] != cur_bird[1]:
            cur_bird = birds[i]
            cnts += 1

print(cnts)

# # 모범답안
# MAX_NUM = 10
# UNDEFINED = -1

# # 변수 선언 및 입력:
# n = int(input())

# # 움직인 비둘기 번호와, 움직인 방향을 기록합니다.
# movements = [
#     tuple(map(int, input().split()))
#     for _ in range(n)
# ]

# # 현재 비둘기의 위치를 기록합니다. 
# # UNDEFINED이면 아직 미정인 상태로,
# # 초기값을 전부 UNDEFINED로 설정합니다.
# pos = [UNDEFINED] * (MAX_NUM + 1)

# move_cnt = 0
# # 입력으로 주어진 움직임에 따라
# # 비둘기 위치를 이동시켜줍니다.
# for pigeon, move_dir in movements:
#     # 해당 비둘기의 위치가 미정이라면
#     if pos[pigeon] == UNDEFINED:
#         # 주어진 첫 번째 위치에서 시작한다고
#         # 생각하는게 비둘기의 이동 횟수를 
#         # 최소로 할 수 있는 방법입니다.
#         pos[pigeon] = move_dir
    
#     # 이미 비둘기의 위치가 정해져 있는데
#     # 옮겨간 위치와 다른 위치라면
#     elif pos[pigeon] != move_dir:
#         # 이동시켜준 뒤,
#         pos[pigeon] = move_dir
#         # 답을 갱신합니다.
#         move_cnt += 1

# print(move_cnt)