A, B = map(int, input().split())
N = int(input())

n_lst = list(map(int, str(N)))
num = 0

for i in range(len(n_lst)):
    num = num * A + n_lst[i]

digits = []
while True:
    if num < B:
        digits.append(num)
        break

    digits.append(num % B)
    num //= B

print("".join(map(str, digits[::-1])))