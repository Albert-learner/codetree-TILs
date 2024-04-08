A, B = map(int, input().split())

def is_prime_number(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False

    return True

prime_sum = 0
for num in range(A, B + 1):
    if is_prime_number(num):
        prime_sum += num

print(prime_sum)