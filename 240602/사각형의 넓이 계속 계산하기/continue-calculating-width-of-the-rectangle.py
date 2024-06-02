while True:
    str_r, str_c, alp = input().split()
    r, c = int(str_r), int(str_c)
    areas = 0

    if alp == 'C':
        areas += (r * c)
        print(areas)
        break
    else:
        areas += (r * c)
    
    print(areas)