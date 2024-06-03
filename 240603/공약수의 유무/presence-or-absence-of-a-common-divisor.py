a, b = map(int, input().split())

first, second = [], []
for i in range(1, int(1920 ** 0.5) + 1):
    if 1920 % i == 0:
        first.append(i)
        if i != 1920 // i:
            first.append(1920 // i)
first = sorted(first)

for i in range(1, int(2880 ** 0.5) + 1):
    if 2880 % i == 0:
        second.append(i)
        if i != 2880 // i:
            second.append(2880 // i)
second = sorted(second)

answer = False
for n in range(a, b + 1):
    if n in first or n in second:
        answer = True

if answer == True:
    print(1)
else:
    print(0)