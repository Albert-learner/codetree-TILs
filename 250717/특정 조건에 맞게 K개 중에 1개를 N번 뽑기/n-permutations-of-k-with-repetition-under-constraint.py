from itertools import product

K, N = map(int, input().split())

def check_3_consecutives(seq):
    count = 1

    for i in range(1, len(seq)):
        if seq[i] == seq[i - 1]:
            count += 1
            if count >= 3:
                return True
        else:
            count = 1

    return False

def generate_valid_combs(k, n):
    digits = [num for num in range(1, k + 1)]
    valid = []

    for comb in product(digits, repeat=n):
        if not check_3_consecutives(comb):
            valid.append(comb)

    return valid

valid_combs = generate_valid_combs(K, N)
for valid_comb in valid_combs:
    print(*valid_comb)