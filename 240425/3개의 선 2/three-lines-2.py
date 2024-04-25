N = int(input())
x, y = [], []
xy = [[0] * 11 for _ in range(11)]
cases = ["xxx", "xxy", "xyx", "yxx", "yyy", "yyx", "yxy", "xyy"]

for _ in range(N):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)
    xy[xi][yi] = 1

def go(n, chr):
    sum_ = 0
    if chr == 'x':
        for i in range(11):
            sum_ += xy[i][n]
    else:
        for i in range(11):
            sum_ += xy[n][i]

    return sum_

for cse in cases:
    c1, c2, c3 = cse[0], cse[1], cse[2]
    for i in range(6):
        for j in range(6):
            for k in range(6):
                if i == j or j == k or k == i:
                    continue

                sum_ = 0
                sum_ += go(i, c1)
                sum_ += go(j, c2)
                sum_ += go(k, c3)

                if sum_ == N:
                    print(1)
                    exit()

print(0)