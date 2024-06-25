cnts = 0

odds_lst = []
while True:
    input_str = input()
    if input_str == '0':
        print(cnts)
        break

    cnts += 1
    if cnts % 2 == 1:
        odds_lst.append(input_str)

for odd in odds_lst:
    print(odd)