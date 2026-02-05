from functools import cmp_to_key

# 변수 선언 및 입력:
n = int(input())
arr = [
    int(input())
    for _ in range(n)
]

# custom comparator를 직접 정의
# a가 앞에 있는 숫자, b가 뒤에 있는 숫자라고 가정했을 때
# 이 순서가 우리가 원하는 순서라면 0보다 작은 값을, 
# 반대라면 0보다 큰 값을
# 둘의 우선순위가 동일하다면 0을 반환하면 됩니다.
# 보통 반환값에 1, -1, 0을 사용합니다.
def compare(a, b):
    # str(a) + str(b) > str(b) + str(a)라면 
    # a가 더 앞에 있어야 하므로
    # 현재 순서가 옳습니다.
    if str(a) + str(b) > str(b) + str(a):
        return -1
    # str(a) + str(b) < str(b) + str(a)라면 
    # b가 더 앞에 있어야 하므로
    # 현재 순서는 틀렸습니다.
    if str(a) + str(b) < str(b) + str(a):
        return 1
    # 우선 순위가 동일한 경우입니다.
    return 0


# a + b 기준 내림차순으로 정렬해줍니다.
# 문자열을 이용하면 편하게 구현이 가능합니다.
arr.sort(key=cmp_to_key(compare))

for elem in arr:
    print(elem, end="")
