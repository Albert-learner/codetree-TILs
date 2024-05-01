N = int(input())
seats = list(map(int, input()))

ones = [idx for idx, cst in enumerate(seats) if cst == 1]

max_dst, start, end = 0, 0, 0
for idx, cst in enumerate(ones):
    if idx == len(ones) - 1:
        break

    if ones[idx + 1] - ones[idx] > max_dst:
        max_dst = ones[idx + 1] - ones[idx]
        start, end = ones[idx], ones[idx + 1]

print(abs(end - start) // 2)