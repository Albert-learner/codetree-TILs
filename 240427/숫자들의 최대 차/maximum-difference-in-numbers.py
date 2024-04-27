N, K = map(int, input().split())
n_lst = [int(input()) for _ in range(N)]
n_lst.sort()

max_cnts = 0
for i in range(N):
    cnts = 1
    for j in range(i + 1, N):
        if abs(n_lst[j] - n_lst[i]) <= K:
            cnts += 1
        else:
            break

    max_cnts = max(max_cnts, cnts)

print(max_cnts)

# # 모범답안
# # 선언 및 입력:
# n, k = tuple(map(int, input().split()))
# arr = [
#     int(input())
#     for _ in range(n)
# ]

# # 구간 [l, r] 
# # 사이에 들어있는 숫자 개수를 반환합니다.
# def count_num(l, r):
#     cnt = 0
#     for elem in arr:
#         if l <= elem and elem <= r:
#             cnt += 1

#     return cnt


# ans = 0
# # 크기가 K인 모든 구간을 잡아
# # 해당 구간 안에 들어오는 숫자의 개수를 세서
# # 그 중 최댓값을 계산합니다.
# for i in range(1, MAX_NUM + 1):
#     # 구간 [i, i + k] 사이에 들어있는 숫자를 세어
#     # 최댓값을 계산합니다.
#     ans = max(ans, count_num(i, i + k))

# print(ans)