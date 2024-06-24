input_str, str_ques = input().split()
ques = [int(input()) for _ in range(int(str_ques))]

for q in ques:
    if q == 1:
        input_str = input_str[1:] + input_str[0]
    elif q == 2:
        input_str = input_str[-1] + input_str[:-1]
    elif q == 3:
        input_str = input_str[::-1]

    print(input_str)