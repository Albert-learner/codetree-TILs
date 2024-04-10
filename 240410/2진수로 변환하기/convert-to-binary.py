N = int(input())

digits_lst = []
while True:
    if N < 2:
        digits_lst.append(N)
        break

    digits_lst.append(N % 2)
    N //= 2

print("".join(map(str, digits_lst[::-1])))