input_str, find_chr = input().split()

if find_chr not in input_str:
    print("No")
else:
    print(input_str.find(find_chr))