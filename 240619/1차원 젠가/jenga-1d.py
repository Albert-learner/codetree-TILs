N = int(input())
blocks = [int(input()) for _ in range(N)]
s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())

blocks = blocks[:s1 - 1] + blocks[e1:]
blocks = blocks[:s2 - 1] + blocks[e2:]
blocks.insert(0, len(blocks))

for n in blocks:
    print(n)

# # 모범답안 1
# # 변수 선언 및 입력
# n = int(input())
# numbers = [
#     int(input())
#     for _ in range(n)
# ]
# end_of_array = n


# # 입력 배열에서 지우고자 하는 부분 수열을 삭제합니다.
# def cut_array(start_idx, end_idx):
#     global end_of_array, numbers
    
#     temp_arr = []
    
#     # 구간 외의 부분만 temp 배열에 순서대로 저장합니다.
#     for i in range(end_of_array):
#         if i < start_idx or i > end_idx:
#             temp_arr.append(numbers[i])

#     # temp 배열을 다시 numbers 배열로 옮겨줍니다.
#     end_of_array = len(temp_arr)
#     for i in range(end_of_array):    
#         numbers[i] = temp_arr[i]


# # 두 번에 걸쳐 지우는 과정을 반복합니다.
# for _ in range(2):
#     s, e = tuple(map(int, input().split()))
#     # [s, e] 구간을 삭제합니다.
#     cut_array(s - 1, e - 1)

# # 출력:
# print(end_of_array)
# for i in range(end_of_array):
#     print(numbers[i])

# # 모범답안 2
# # 변수 선언 및 입력
# n = int(input())
# numbers = [
#     int(input())
#     for _ in range(n)
# ]
# end_of_array = n


# # 입력 배열에서 지우고자 하는 부분 수열을 삭제합니다.
# def cut_array(start_idx, end_idx):
#     global end_of_array
    
#     cut_len = end_idx - start_idx + 1;
#     for i in range(end_idx + 1, end_of_array):
#         numbers[i - cut_len] = numbers[i]
    
#     end_of_array -= cut_len


# # 두 번에 걸쳐 지우는 과정을 반복합니다.
# for _ in range(2):
#     s, e = tuple(map(int, input().split()))
#     # [s, e] 구간을 삭제합니다.
#     cut_array(s - 1, e - 1)

# # 출력:
# print(end_of_array)
# for i in range(end_of_array):
#     print(numbers[i])