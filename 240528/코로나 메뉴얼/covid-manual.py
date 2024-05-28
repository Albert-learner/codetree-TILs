first = input().split()
second = input().split()
third = input().split()

first[1], second[1], third[1] = int(first[1]), int(second[1]), int(third[1])

emergency = 0
for person in [first, second, third]:
    if person[0] == 'Y' and person[1] >= 37:
        emergency += 1

if emergency >= 2:
    print('E')
else:
    print('N')