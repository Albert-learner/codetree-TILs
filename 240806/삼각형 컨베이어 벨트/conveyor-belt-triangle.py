# My Solution
N, T = map(int, input().split())
belt = [list(map(int, input().split())) for _ in range(3)]

while T > 0:
    lasts = [belt[2][-1], belt[0][-1], belt[1][-1]]
    for r_idx, last in zip(range(len(belt)), lasts):
        belt[r_idx] = [last] + belt[r_idx][:-1]
    T -= 1

for row in belt:
    print(*row)

# # Other Solution
# N, T = map(int, input().split())
# belt = [list(map(int, input().split())) for _ in range(3)]
# first, second, third = belt[0], belt[1], belt[2]

# while T > 0:
#     second.insert(0, first.pop())
#     third.insert(0, second.pop())
#     first.insert(0, third.pop())
#     T -= 1

# print(*first)
# print(*second)
# print(*third)

# # 모범답안
# # 변수 선언 및 입력
# n, t = tuple(map(int, input().split()))
# l = list(map(int, input().split()))
# r = list(map(int, input().split()))
# d = list(map(int, input().split()))

# for _ in range(t):
#     # Step 1
#     # 왼쪽에서 가장 오른쪽에 있는 숫자를 따로 temp값에 저장해놓습니다.
#     temp = l[n - 1]
    
#     # Step 2
#     # 왼쪽에 있는 숫자들을 완성합니다. 
#     # 벨트를 기준으로 오른쪽에서부터 채워넣어야 하며, 
#     # 맨 왼쪽 숫자는 아래에서 가져와야함에 유의합니다.
#     for i in range(n - 1, 0, -1):
#         l[i] = l[i - 1]
#     l[0] = d[n - 1]
    
#     # Step 3
#     # 오른쪽에 있는 숫자들을 완성합니다. 
#     # 벨트를 기준으로 마찬가지로 오른쪽에서부터 채워넣어야 하며, 
#     # 맨 왼쪽 숫자는 이전 단계에서 미리 저장해놨던 temp값을 가져와야함에 유의합니다.
#     temp2 = r[n - 1]
#     for i in range(n - 1, 0, -1):
#         r[i] = r[i - 1]
#     r[0] = temp
    
#     # Step 4
#     # 아래에 있는 숫자들을 완성합니다. 
#     # 마찬가지로 벨트를 기준으로 오른쪽에서부터 채워넣어야 하며, 
#     # 맨 왼쪽 숫자는 이전 단계에서 미리 저장해놨던 temp값을 가져와야함에 유의합니다.
#     for i in range(n - 1, 0, -1):
#         d[i] = d[i - 1]
#     d[0] = temp2
    
# # 출력
# for elem in l:
#     print(elem, end=" ")
# print()

# for elem in r:
#     print(elem, end=" ")
# print()

# for elem in d:
#     print(elem, end=" ")