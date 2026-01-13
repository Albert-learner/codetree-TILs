import sys

INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize

# 변수 선언 및 입력:
m = int(input())
a, b = tuple(map(int, input().split()))

min_ans, max_ans = INT_MAX, INT_MIN


def get_try_num(target):
    left, right = 1, m
    cnt = 0
    while left <= right:
        mid = (left + right) // 2
        cnt += 1

        if mid == target:
            return cnt
        
        if mid > target:
            right = mid - 1
        else:
            left = mid + 1

    return -1

   
# 컴퓨터가 선택한 수를
# a부터 b까지 각각 가정해보며
# 그 중 최소 횟수와 최대 횟수를 구합니다.
for i in range(a, b + 1):
    # 이진탐색을 진행하여 진행 횟수를 구합니다.
    num = get_try_num(i)
    # 답을 갱신합니다.
    min_ans = min(min_ans, num)
    max_ans = max(max_ans, num)

print(min_ans, max_ans)
