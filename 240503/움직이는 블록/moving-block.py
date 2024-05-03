N = int(input())
blocks = [int(input()) for _ in range(N)]

sum_blocks = sum(blocks)
average = sum_blocks // N

cnts = 0
while blocks.count(average) < N:
    blocks.sort()

    diff = average - blocks[0]
    diff_max = abs(average - blocks[-1])
    blocks[0] += diff
    blocks[-1] -= diff_max

    cnts += diff

print(cnts)

# # 모범답안
# # 변수 선언 및 입력:
# n = int(input())
# blocks = [
#     int(input())
#     for _ in range(n)
# ]

# # 전체 블럭 수를 셉니다.
# sum_of_blocks = sum(blocks)

# # 평균 블럭 수 보다 더 큰 블럭에 대해서만
# # 그 차이만큼 옮겨주면 됩니다.
# avg = sum_of_blocks // n
# ans = 0
# for block_num in blocks:
#     if block_num > avg:
#         ans += block_num - avg

# print(ans)