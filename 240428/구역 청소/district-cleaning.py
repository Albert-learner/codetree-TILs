a, b = map(int, input().split())
c, d = map(int, input().split())

if b >= c:
    a_areas = list(range(a, b + 1))
    b_areas = list(range(c, d + 1))

    total_areas = sorted(list(set(a_areas + b_areas)))
    print(total_areas[-1] - total_areas[0])
else:
    a_areas = list(range(a + 1, b + 1))
    b_areas = list(range(c + 1, d + 1))

    print(len(a_areas) + len(b_areas))