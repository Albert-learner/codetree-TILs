N, T = map(int, input().split())
n_lst = list(map(int, input().split()))

answer, cnts, num = 0, 0, 0
for i in range(N):
    n_new = n_lst[i]
    if n_new > T:
        cnts += 1
    else:
        cnts = 0

    answer = max(answer, cnts)
    num = n_new

print(answer)

# # 모범답안
# # 변수 선언 및 입력:
# n, t = tuple(map(int, input().split()))
# arr = list(map(int, input().split()))
   
# # 연속하여 t보다 큰 숫자가 나오는 횟수를 구해보며,
# # 그 중 최댓값을 갱신합니다.
# ans, cnt = 0, 0
# for i in range(n):
#     # Case 1
#     if arr[i] > t:
#         cnt += 1
#     # Case 2
#     else:
#         cnt = 0
    
#     ans = max(ans, cnt)

# print(ans)