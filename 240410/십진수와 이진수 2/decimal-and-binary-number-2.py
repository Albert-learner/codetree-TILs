bin_number = input()

num = 0
for idx in range(len(bin_number)):
    num = num * 2 + int(bin_number[idx])


num *= 17
digits = []
while True:
    if num < 2:
        digits.append(num)
        break

    digits.append(num % 2)
    num //= 2

print("".join(map(str, digits[::-1])))