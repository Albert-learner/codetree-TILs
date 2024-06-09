N = int(input())

def is_prime_number(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

prime_numbers = []
for i in range(2, N + 1):
    if is_prime_number(i):
        prime_numbers.append(i)

print(*prime_numbers)