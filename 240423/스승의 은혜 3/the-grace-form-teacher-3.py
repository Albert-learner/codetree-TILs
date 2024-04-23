N, B = map(int, input().split())
gifts_info = [list(map(int, input().split())) for _ in range(N)]

max_students = 0
for i in range(N):
    gifts_info[i][0] //= 2
    prices = [(gifts_info[j][0] + gifts_info[j][1]) for j in range(N)]
    gifts_info[i][0] *= 2
    prices.sort()

    students, cur_prices = 0, 0

    for j in range(N):
        if cur_prices + prices[j] > B:
            break

        cur_prices += prices[j]
        students += 1

    max_students = max(max_students, students)

print(max_students)


# # 답안
# n, b = map(int, input().split())
# wishes = [tuple(map(int, input().split())) for _ in range(n)]

# ans = 0
# for i in range(n):
#     tmp = [list(wishes[j]) for j in range(n)]

#     tmp[i][0] /= 2

#     prices = [(tmp[k][0] + tmp[k][1]) for k in range(n)]
#     prices.sort()

#     student = 0
#     cnt = 0

#     for x in range(n):
#         if cnt + prices[x] > b:
#             break
#         cnt += prices[x]
#         student += 1

#     ans = max(ans, student)

# print(ans)