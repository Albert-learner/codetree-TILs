ans = evaluate()  # 세로선을 가장 왼쪽(예: x=0) 쪽에 둔 경우도 고려

i = 0
while i < n:
    cur_x = points[i][0]

    # 세로선을 x = cur_x + 1 로 옮긴다고 생각하면,
    # x == cur_x 인 점들은 이제 왼쪽으로 넘어감
    while i < n and points[i][0] == cur_x:
        _, y = points[i]
        right[y] -= 1
        left[y] += 1
        i += 1

    ans = min(ans, evaluate())

print(ans)