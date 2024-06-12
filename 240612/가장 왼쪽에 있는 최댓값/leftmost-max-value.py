# N = int(input())
# n_lst = list(map(int, input().split()))

# while len(n_lst) >= 1:
#     max_cst = max(n_lst)

#     idx = 0
#     for i in range(len(n_lst)):
#         if n_lst[i] == max_cst:
#             idx = i
#             break

#     print(idx + 1, end = ' ')
#     n_lst = n_lst[:idx]

# 모범답안 1
# 변수 선언 및 입력
n = int(input())
a = list(map(int, input().split()))

prev_max_idx = n

# 첫 번째 원소가 최대가 되기 전까지 계속 반복합니다.
while True:
    # 최대값 후보의 시작은 항상 첫 번째 원소입니다.
    max_idx = 0

    # 두 번째 원소부터 바로 직전 최대로 뽑힌
    # 원소 전까지 보면서 그 중 최대 index를 갱신합니다.
    # index를 오름차순으로 보기 때문에
    # 최댓값이 여러개인 경우 가장 왼쪽에 있는
    # 원소가 뽑히게 됩니다.
    for i in range(1, prev_max_idx):
        if a[i] > a[max_idx]:
            max_idx = i

    print(max_idx + 1, end=" ")

    # 최대인 원소가 첫 번째 원소라면 종료합니다.
    if max_idx == 0:
        break

    #바로 직전 최대 index를 갱신해줍니다.
    prev_max_idx = max_idx