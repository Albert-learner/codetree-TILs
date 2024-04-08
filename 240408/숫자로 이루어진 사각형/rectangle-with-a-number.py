def print_rectangle(n):
    quota, rest = divmod(n ** 2, 9)
    nums_lst = quota * list(range(1, 10)) + list(range(1, rest + 1))

    for num_idx, num in enumerate(nums_lst, 1):
        if num_idx % n == 0:
            print(num)
        else:
            print(num, end = ' ')
    

N = int(input())
print_rectangle(N)

# # 모범 답안
# row_num = int(input())

# # n개의 줄에 걸쳐 특정 문자열을 출력하는 함수입니다.
# def print_num(n):
#     cnt = 1
#     for _ in range(n):
#         for _ in range(n):
#             print(cnt, end=" ")
#             cnt += 1
#             if cnt == 10:
#                 cnt = 1
#         print()

# print_num(row_num)