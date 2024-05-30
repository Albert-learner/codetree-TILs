a, b = map(int, input().split())

print(f"{a // b}.", end = '')
a %= b

for _ in range(20):
    a *= 10
    print(a // b, end = '')

    a %= b

# # Not My Solution
# quota = a // b
# print(f"{quota}.", end = '')

# cnts = 0
# while cnts < 20:
#     if quota * b == a:
#         print(0, end = '')
#     elif quota == 0:
#         a *= 10
#         print(a // b, end = '')
#         quota = a // b
#     else:
#         a = (a - quota * b) * 10
#         print(a // b, end = '')
#         quota = a // b

#     cnts += 1