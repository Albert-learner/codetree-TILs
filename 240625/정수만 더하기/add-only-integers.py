a_str = input()

total = 0
for a_chr in a_str:
    if a_chr.isdigit():
        total += int(a_chr)

print(total)