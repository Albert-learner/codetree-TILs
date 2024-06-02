while True:
    str_r, str_c, alp = input().split()
    r, c = int(str_r), int(str_c)
    areas = r * c

    print(areas)
    if alp == 'C':
        break