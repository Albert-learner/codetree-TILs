MAX_C = 3

# 변수 선언 및 입력:
n, q = tuple(map(int, input().split()))
arr = [0] + [
    int(input())
    for _ in range(n)
]

prefix_sum = [
    [0] * (n + 1)
    for _ in range(MAX_C + 1)
]


# 번호가 c인 돌 중 [s, e] 구간 내의 원소의 합을 반환합니다.
def get_sum(c, s, e):
    return prefix_sum[c][e] - prefix_sum[c][s - 1]


# 누적합 배열을 만들어줍니다.
# prefix_sum[i][j] : 번호가 i인 돌에 대한 누적합을 저장합니다.
for i in range(1, 4):
    prefix_sum[i][0] = 0
    for j in range(1, n + 1):
        # arr[j]가 i라면, 개수가 하나 더 증가합니다.
        if arr[j] == i:
            prefix_sum[i][j] = prefix_sum[i][j - 1] + 1
        else:
            prefix_sum[i][j] = prefix_sum[i][j - 1]

# q개의 질의에 대해
# 각 돌의 개수를 출력합니다.
for _ in range(q):
    a, b = tuple(map(int, input().split()))
    print(get_sum(1, a, b), get_sum(2, a, b), get_sum(3, a, b))
