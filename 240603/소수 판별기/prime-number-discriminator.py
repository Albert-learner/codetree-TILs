N = int(input())

def is_prime_number(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False

    return True

if is_prime_number(N):
    print('P')
else:
    print('C')