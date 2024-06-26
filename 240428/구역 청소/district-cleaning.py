a, b = map(int, input().split())
c, d = map(int, input().split())

if a > c and b > d:
    a, b, c, d = c, d, a, b

if b >= c:
    a_areas = list(range(a, b + 1))
    b_areas = list(range(c, d + 1))

    total_areas = sorted(list(set(a_areas + b_areas)))
    print(total_areas[-1] - total_areas[0])
else:
    a_areas = list(range(a, b))
    b_areas = list(range(c, d))
    print(len(a_areas) + len(b_areas))