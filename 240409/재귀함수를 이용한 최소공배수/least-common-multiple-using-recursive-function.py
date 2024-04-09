N = int(input())
n_lst = list(map(int, input().split()))

def GCD(a, b):
    if a % b == 0:
        return b

    return GCD(b, a % b)

def LCM(n):
    if n == 0:
        return n_lst[0]
    elif n == 1:
        return (n_lst[0] * n_lst[1]) // (GCD(n_lst[0], n_lst[1]))

    minus = LCM(n - 1)
    return minus * n_lst[n] // GCD(minus, n_lst[n])

print(LCM(N - 1))

# # 모범 답안
# # 변수 선언 및 입력:
# n = int(input())
# arr = [0] + list(map(int, input().split()))


# # 두 수간의 최소공배수를 구하여 반환합니다.
# def lcm(a, b):
#     gcd = 1
#     for i in range(1, min(a, b) + 1):
#         if a % i == 0 and b % i == 0:
#             gcd = i

#     return a * b // gcd


# # index번째 까지 인덱스의 숫자 중에 가장 큰 값을 반환합니다.
# def get_lcm_all(index):
#     # 남은 원소가 1개라면 그 자신이 답이 됩니다.
#     if index == 1:
#         return arr[1]

#     # 1번째 ~ index - 1번째 원소의 최소공배수를 구한 결과와
#     # 현재 index 원소의 최소공배수를 구하여 반환합니다.
#     return lcm(get_lcm_all(index - 1), arr[index])

   
# # 모든 수의 최소공배수를 구합니다.
# print(get_lcm_all(n))