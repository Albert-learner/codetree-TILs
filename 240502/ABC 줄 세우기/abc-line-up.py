N = int(input())
line = input().split()

def bubble_sort(lst):
    cnts = 0
    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                cnts += 1

    return cnts, lst

total_cnts, sort_line = bubble_sort(line)
print(total_cnts)

# # 모범답안
# # 변수 선언 및 입력:
# n = int(input())
# arr = [0] + list(input().split())
# ans = 0

# # 'A' 부터 알파벳 순서대로 찾아 가장 앞으로 이동합니다.
# for i in range(1, n + 1):
#     x = chr(ord('A') + i - 1)

#     # i번째 알파벳을 찾아 idx에 저장합니다.
#     idx = 0
#     for j in range(1, n + 1):
#         if arr[j] == x:
#             idx = j
    
#     # idx번째 알파벳을 i번째 위치까지 swap합니다.
#     for j in range(idx - 1, i - 1, -1):
#         arr[j], arr[j + 1] = arr[j + 1], arr[j]
#         ans += 1

# print(ans)