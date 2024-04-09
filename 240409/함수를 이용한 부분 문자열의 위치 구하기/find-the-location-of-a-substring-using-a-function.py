input_str = input()
p_str = input()

if p_str in input_str:
    print(input_str.index(p_str))
else:
    print(-1)