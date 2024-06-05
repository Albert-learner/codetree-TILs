N = int(input())

for i in range(N):
    if i == 0:
        for _ in range(N):
            print('*', end = ' ')
    else:
        for j in range(N):
            if j % 2 == 1 and j >= i:
                print('*', end = ' ')
            else:
                print(' ', end = ' ')
    print()

# # 모범답안
# for i in range(n):
#     for j in range(n):
#         if j % 2 == 0:
#             if i == 0:
#                 print("* ", end="")
#             else:
#                 print("  ", end="")
#         else:
#             if i <= j:
#                 print("* ", end="")
#             else:
#                 print("  ", end="")
#     print()