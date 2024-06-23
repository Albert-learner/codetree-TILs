s_str, str_q = input().split()
questions = int(str_q)
ques = [input().split() for _ in range(questions)]

s_str_lst = list(s_str)
for n, a, b in ques:
    if n == '1':
        a_int, b_int = int(a), int(b)
        s_str_lst[a_int - 1], s_str_lst[b_int - 1] = s_str_lst[b_int - 1], s_str_lst[a_int - 1]
    elif n == '2':
        for idx, s_str in enumerate(s_str_lst):
            if s_str == a:
                s_str_lst[idx] = b

    print("".join(s_str_lst))