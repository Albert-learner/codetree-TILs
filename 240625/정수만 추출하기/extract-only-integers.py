first, second = input().split()

first_int, second_int = 0, 0
first_str, second_str = "", ""
for f_str in first:
    if not f_str.isdecimal():
        break

    first_str += f_str

for s_str in second:
    if not s_str.isdecimal():
        break
    
    second_str += s_str

first_int, second_int = int(first_str), int(second_str)
print(first_int + second_int)