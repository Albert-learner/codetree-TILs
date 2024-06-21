find_chr = input()

five_strs = ["apple", "banana", "grape", "blueberry", "orange"]

answer = 0
for one_str in five_strs:
    if one_str[2] == find_chr or one_str[3] == find_chr:
        print(one_str)    
        answer += 1

print(answer)