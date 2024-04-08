A, B = map(int, input().split())

def count_onjeonsus(a, b):
    onjeonsus = []

    for num in range(a, b + 1):
        if num % 2 != 0 and int(str(num)[-1]) != 5 and (num % 3 != 0 or num % 9 == 0):
            onjeonsus.append(num)

    return len(onjeonsus)

print(count_onjeonsus(A, B))