N, M = map(int, input().split())
bombs = [int(input()) for _ in range(N)]

def get_consecutive_counts(bombs):
    n = len(bombs)
    consecutive_cnts = [0] * n
    cnts = 0
    for i in range(n - 1, 0, -1):
        if bombs[i] == bombs[i - 1]:
            cnts += 1
        else:
            cnts = 0
        consecutive_cnts[i] = cnts
    
    return consecutive_cnts

def can_bomb(consecutive_cnts, m):
    return any(cnts >= m - 1 for cnts in consecutive_cnts)

def explode(bombs, consecutive_cnts, m):
    if m == 1:
        return []

    n = len(bombs)
    bombed = [0] * n
    for i, cnts in enumerate(consecutive_cnts):
        if cnts >= m - 1:
            for j in range(i - 1, i + cnts):
                bombed[j] = 1

    return [bombs[i] for i in range(n) if not bombed[i]]

while True:
    consecutive_cnts = get_consecutive_counts(bombs)
    if not can_bomb(consecutive_cnts, M):
        break

    bombs = explode(bombs, consecutive_cnts, M)

print(len(bombs))
for bomb in bombs:
    print(bomb)

# # 모범답안 1(시뮬레이션)
# # 변수 선언 및 입력
# n, m = tuple(map(int, input().split()))
# numbers = [
#     int(input())
#     for _ in range(n)
# ]


# # 주어진 시작점에 대하여
# # 부분 수열의 끝 위치를 반환합니다.
# def get_end_idx_of_explosion(start_idx, curr_num):
#     for end_idx in range(start_idx + 1, len(numbers)):
#         if numbers[end_idx] != curr_num:
#             return end_idx - 1
        
#     return len(numbers) - 1


# while True:
#     did_explode = False
    
#     for curr_idx, number in enumerate(numbers):
#         # 각 위치마다 그 뒤로 폭탄이 m개 이상 있는지 확인합니다.
			
# 		# 이미 터지기로 예정되어있는 폭탄은 패스합니다.
#         if number == 0:
#             continue
#         # curr_idx로부터 연속하여 같은 숫자를 갖는 폭탄 중 
# 		# 가장 마지막 위치를 찾아 반환합니다.
#         end_idx = get_end_idx_of_explosion(curr_idx, number)
        
#         if end_idx - curr_idx + 1 >= m:
#             # 연속한 숫자의 개수가 m개 이상인 경우 폭탄이 터졌음을 기록해줍니다.
#             # 터져야 할 폭탄들에 대해 터졌다는 의미로 0을 채워줍니다.
#             numbers[curr_idx:end_idx + 1] = [0] * (end_idx - curr_idx + 1)
#             did_explode = True
        
#     # 폭탄이 터진 이후의 결과를 계산하여 반영해줍니다.
#     numbers = list(filter(lambda x: x > 0, numbers))
    
#     # 더 이상 폭탄이 터지지 않는다면 종료합니다.
#     if not did_explode:
#         break

# print(len(numbers))
# for number in numbers:
#     print(number)

# # 모범답안 2(시뮬레이션 + Memory Optimization)
# # 변수 선언 및 입력
# n, m = tuple(map(int, input().split()))
# numbers = [
#     int(input())
#     for _ in range(n)
# ]


# # 주어진 시작점에 대하여
# # 부분 수열의 끝 위치를 반환합니다.
# def get_end_idx_of_explosion(start_idx, curr_num):
#     for end_idx in range(start_idx + 1, len(numbers)):
#         if numbers[end_idx] != curr_num:
#             return end_idx - 1
        
#     return len(numbers) - 1


# while True:
#     did_explode = False
#     curr_idx = 0
    
#     while curr_idx < len(numbers):
#         end_idx = get_end_idx_of_explosion(curr_idx, numbers[curr_idx])
        
#         if end_idx - curr_idx + 1 >= m:
#             # 연속한 숫자의 개수가 m개 이상이면
#             # 폭탄이 터질 수 있는 경우 해당 부분 수열을 잘라내고
#             # 폭탄이 터졌음을 기록해줍니다.
#             del numbers[curr_idx:end_idx + 1]
#             did_explode = True
#         else:
#             # 주어진 시작 원소에 대하여 폭탄이 터질 수 없는 경우
#             # 다음 원소에 대하여 탐색하여 줍니다.
#             curr_idx += 1

#     if not did_explode:
#         break

# print(len(numbers))
# for number in numbers:
#     print(number)

# # 모범답안 3(시뮬레이션 + Memory Optimization + Time Optimization)
# # 변수 선언 및 입력
# n, m = tuple(map(int, input().split()))
# numbers = [
#     int(input())
#     for _ in range(n)
# ]


# # 주어진 시작점에 대하여
# # 부분 수열의 끝 위치를 반환합니다.
# def get_end_idx_of_explosion(start_idx, curr_num):
#     for end_idx in range(start_idx + 1, len(numbers)):
#         if numbers[end_idx] != curr_num:
#             return end_idx - 1
        
#     return len(numbers) - 1


# while True:
#     did_explode = False
#     curr_idx = 0
    
#     while curr_idx < len(numbers):
#         end_idx = get_end_idx_of_explosion(curr_idx, numbers[curr_idx])
        
#         if end_idx - curr_idx + 1 >= m:
#             # 연속한 숫자의 개수가 m개 이상이면
#             # 폭탄이 터질 수 있는 경우 해당 부분 수열을 잘라내고
#             # 폭탄이 터졌음을 기록해줍니다.
#             del numbers[curr_idx:end_idx + 1]
#             did_explode = True
#         else:
#             # 주어진 시작 원소에 대하여 폭탄이 터질 수 없는 경우
#             # 다음 원소에 대하여 탐색하여 줍니다.
#             curr_idx = end_idx + 1

#     if not did_explode:
#         break

# print(len(numbers))
# for number in numbers:
#     print(number)