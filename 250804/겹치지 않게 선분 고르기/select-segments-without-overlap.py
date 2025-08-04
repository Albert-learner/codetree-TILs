n = int(input())
lines = [list(map(int, input().split())) for _ in range(n)]
lines.sort()

def calc_lines():
    if 1 not in flag:
        return 0

    last, cnts = -1, 0
    for i in range(n):
        if flag[i]:
            if last == -1:
                last = lines[i][1]
                cnts += 1
            else:
                if last < lines[i][0]:
                    last = lines[i][1]
                    cnts += 1

    return cnts

def including_line(now, most_cnts):
    if now == n:
        cnts = calc_lines()
        if most_cnts < cnts:
            most_cnts = cnts
        return most_cnts

    for i in range(2):
        flag.append(i)
        most_cnts = including_line(now + 1, most_cnts)
        flag.pop()

    return most_cnts

flag = []
print(including_line(0, 0))