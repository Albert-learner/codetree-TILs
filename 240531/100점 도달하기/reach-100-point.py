N = int(input())

for i in range(N, 101):
    if i < 60:
        print('F', end = ' ')
    elif 60 <= i < 70:
        print('D', end = ' ')
    elif 70 <= i < 80:
        print('C', end = ' ')
    elif 80 <= i < 90:
        print('B', end = ' ')
    elif 90 <= i <= 100:
        print('A', end = ' ')