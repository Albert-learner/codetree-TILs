input_str = input()

s_len = len(input_str)

for i in range(s_len + 1):
    print(input_str[-i:] + input_str[:-i])