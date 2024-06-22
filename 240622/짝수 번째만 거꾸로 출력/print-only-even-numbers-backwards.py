input_str = input()

eval_strs = [ip_chr for idx, ip_chr in enumerate(input_str, 1) if idx % 2 == 0]

print("".join(eval_strs[::-1]))