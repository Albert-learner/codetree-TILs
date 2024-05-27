first = input().split()
second = input().split()

first[0] = int(first[0])
second[0] = int(second[0])

if first[0] >= 19 and first[1] == 'M' or second[0] >= 19 and second[1] == 'M':
    print(1)
else:
    print(0)