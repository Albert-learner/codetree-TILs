input_str = input()

for inp_chr in input_str:
    if inp_chr.islower():
        print(inp_chr.upper(), end = '')
    elif inp_chr.isupper():
        print(inp_chr.lower(), end = '')