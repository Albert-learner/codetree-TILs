import sys
from bisect import bisect_left, bisect_right

input = sys.stdin.readline

# 변수 선언 및 입력:
n, q = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(q)]

# 점들을 정렬합니다.
# (모든 점이 서로 다른 위치라고 했으니 set은 굳이 안 써도 됨)
nums = sorted(arr)

# 각 질의 [a, b]마다 이분 탐색으로 개수를 구합니다.
for a, b in queries:
    left = bisect_left(nums, a)   # x >= a 인 첫 인덱스
    right = bisect_right(nums, b) # x > b 인 첫 인덱스
    print(right - left)
