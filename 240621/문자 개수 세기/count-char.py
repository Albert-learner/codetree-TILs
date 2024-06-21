input_str = input()
find_chr = input()

answer = 0
for inp_chr in input_str:
    if inp_chr == find_chr:
        answer += 1

print(answer)