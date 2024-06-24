input_str = input()

first_idx = input_str.find('e')
print(input_str[:first_idx] + input_str[first_idx + 1:])