arr_cnts = [0] * 4
temps = [0] * 3
symptoms = [''] * 3

for i in range(3):
    symptoms[i], temps[i] = input().split()
    temps[i] = int(temps[i])

for i in range(3):
    if symptoms[i] == 'Y' and temps[i] >= 37:
        arr_cnts[0] += 1
    elif symptoms[i] == 'N' and temps[i] >= 37:
        arr_cnts[1] += 1
    elif symptoms[i] == 'Y' and temps[i] < 37:
        arr_cnts[2] += 1
    elif symptoms[i] == 'N' and temps[i] < 37:
        arr_cnts[3] += 1

for cnts in arr_cnts:
    print(cnts, end = ' ')

if arr_cnts[0] >= 2:
    print('E')