A, B = map(int, input().split())

def is_prime_number(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    
    return True

if A == 1 and B == 1:
    print(0)
else:
    prime_sum = 0
    for num in range(A, B + 1):
        if is_prime_number(num):
            prime_sum += num

    print(prime_sum)

# 모범 답안
# # 변수 선언 및 입력:
# a, b = tuple(map(int, input().split()))


# def is_prime(n):
#     if n == 1:
#         return False

#     for i in range(2, n):
#         if n % i == 0:
#             return False

#     return True


# sum_val = 0
# for i in range(a, b + 1):
#     if is_prime(i):
#         sum_val += i

# print(sum_val)