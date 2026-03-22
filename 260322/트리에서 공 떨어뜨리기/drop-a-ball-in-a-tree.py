n = int(input())
left_num = [-1] + [0] * n
right_num = [-1] + [0] * n

for i in range(1, n + 1):
    left_num[i], right_num[i] = map(int, input().split())

k = int(input())

# Please write your code here.
cur = 1

while True:
    left = left_num[cur]
    right = right_num[cur]

    if left == -1 and right == -1:
        print(cur)
        break

    if left == -1:
        cur = right
    elif right == -1:
        cur = left
    else:
        if k % 2 == 1:
            cur = left
            k = (k + 1) // 2
        else:
            cur = right
            k //= 2