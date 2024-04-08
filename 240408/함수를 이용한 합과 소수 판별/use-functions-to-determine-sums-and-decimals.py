A, B = map(int, input().split())

def is_prime_number(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False

    return True

cnts = 0
for num in range(A, B + 1):
    if is_prime_number(num):
        num_sum = sum([int(n_str) for n_str in str(num)])
        if num_sum % 2 == 0:
            cnts += 1

print(cnts)