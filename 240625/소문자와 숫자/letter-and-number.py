input_str = input()

for inp_chr in input_str:
    if inp_chr.isalpha() or inp_chr.isdigit():
        print(inp_chr.lower(), end = '')