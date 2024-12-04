N = int(input())

def chooses(cnt, num, beaut_arr):
    if cnt >= num:
        if cnt == num:
            beaut_arr[0] += 1
        return

    for i in range(1, 5):
        chooses(cnt + i, num, beaut_arr)

beautiful_arr = [0]
chooses(0, N, beautiful_arr)
print(beautiful_arr[0])