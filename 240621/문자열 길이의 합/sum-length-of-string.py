N = int(input())
input_strs = [input() for _ in range(N)]

total_lengths, a_cnts = 0, 0
for input_str in input_strs:
    total_lengths += len(input_str)
    if input_str.startswith('a'):
        a_cnts += 1

print(total_lengths, a_cnts)