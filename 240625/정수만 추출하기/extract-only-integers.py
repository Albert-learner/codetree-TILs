first, second = input().split()

first_int, second_int = 0, 0
first_str, second_str = "", ""
for f_str in first:
    if not f_str.isdigit():
        first_int += int(first_str)
        break
    else:
        first_str += f_str

for s_str in second:
    if not s_str.isdigit():
        second_int += int(second_str)
        break
    else:
        second_str += s_str

print(first_int + second_int)