a_str = input()
b_str = input()

b_len = len(b_str)
while b_str in a_str:
    b_idx = a_str.find(b_str)
    a_str = a_str[:b_idx] + a_str[b_idx + b_len:]

print(a_str)