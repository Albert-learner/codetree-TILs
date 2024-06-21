input_str = input().split()

answer = 0
for inp_str in input_str:
    answer += len(inp_str)

print(answer)