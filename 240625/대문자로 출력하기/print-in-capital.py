input_str = input()

for inp_chr in input_str:
    if inp_chr.isalpha():
        print(inp_chr.upper(), end = '')