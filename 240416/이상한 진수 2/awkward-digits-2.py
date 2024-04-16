a_bin = list(map(int, input()))

indicator = True
for i in range(len(a_bin)):
    if a_bin[i] == 0:
        a_bin[i] = 1
        indicator = False
        break

num = 0
for i in range(len(a_bin)):
    num = num * 2 + a_bin[i]

if indicator:
    print(num - 1)
else:
    print(num)