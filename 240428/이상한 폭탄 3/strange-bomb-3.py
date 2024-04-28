N, K = map(int, input().split())
bombs = [int(input()) for _ in range(N)]

last_idx = {}
explosions = {}

for i in range(N):
    if bombs[i] in last_idx:
        if i - last_idx[bombs[i]] <= K:
            explosions[bombs[i]] = explosions.get(bombs[i], 0) + 1

    last_idx[bombs[i]] = i

max_explosion = float("inf")
for idx in explosions.keys():
    if max_explosion == float("inf") or explosions[max_explosion] < explosions[idx]:
        max_explosion = idx
    elif explosions[max_explosion] == explosions[idx] and max_explosion < idx:
        max_explosion = idx

print(max_explosion if max_explosion != float("inf") else 0)

# # 모범답안
# MAX_A = 1000000

# # 변수 선언 및 입력
# n, k = tuple(map(int, input().split()))

# num = [
#     int(input())
#     for _ in range(n)
# ]

# bomb = [0] * (MAX_A + 1)
# explode = [False] * n

# maxval = 1
# maxidx = 0

# # 모든 쌍에 대해서 터질 수 있는 폭탄을 찾고
# # 터진 폭탄의 개수를 저장합니다.
# for i in range(n):
#     for j in range(i + 1, n):
#         # 거리가 k를 초과하는 경우 넘어갑니다.
#         if j - i > k:
#             break

#         # 두 폭탄의 번호가 다를 경우 터지지 않습니다.
#         if num[i] != num[j]:
#             continue

#         # 두 폭탄의 번호가 같을 경우 폭탄은 터집니다.
#         # 해당 폭탄이 이미 터진 폭탄인지 확인하고,
#         # 아직 터지지 않은 폭탄이라면 터진 폭탄의 개수를 갱신합니다.
#         if explode[i] == False:
#             bomb[num[i]] += 1;
#             explode[i] = True

#         if explode[j] == False:
#             bomb[num[j]] += 1;
#             explode[j] = True

# for i in range(MAX_A + 1):
#     if maxval <= bomb[i]:
#         maxval = bomb[i]
#         maxidx = i

# print(maxidx)