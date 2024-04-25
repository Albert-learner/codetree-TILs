A, B, C = map(int, input().split())

max_result = 0
for i in range(1000):
    if A * i > C:
        break

    tmp_result = A * i
    for j in range(1000):
        if A * i + B * j > C:
            max_result = max(max_result, tmp_result + B * (j - 1))
            break

print(max_result)