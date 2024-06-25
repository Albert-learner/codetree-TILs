first = input()
second = input()

first_num_str, second_num_str = "", ""
for f_str in first:
    if f_str.isdigit():
        first_num_str += f_str

for s_str in second:
    if s_str.isdigit():
        second_num_str += s_str

print(int(first_num_str) + int(second_num_str))