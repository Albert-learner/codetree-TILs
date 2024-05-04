N = int(input())
n_lst = list(map(int, input().split()))

answer = 0
odds, evens = 0, 0
for n in n_lst:
    if n % 2 != 0:
        odds += 1
    else:
        evens += 1

if evens > odds:
    answer = odds * 2 + 1
elif evens == odds:
    answer = evens + odds
else:
    answer = evens * 2 
    diff = odds - evens

    if diff % 3 == 0:
        answer += (diff // 3) * 2
    else:
        if (diff % 3) % 2 == 0:
            answer += diff // 3 * 2 + 1
        else:
            answer += diff // 3 * 2 - 1

print(answer)

# # 풀이(정답)
# n = int(input())
# ans = 0

# odd = 0
# even = 0

# numbers = list(map(int, input().split()))

# for num in numbers:
#     if num % 2 != 0:
#         odd += 1
#     else:
#         even += 1

# if even > odd:
#     ans = odd * 2 + 1
# elif even == odd:
#     ans = even + odd
# else:
#     ans = even * 2
#     size = odd - even

#     if size % 3 == 0:
#         ans += (size // 3) * 2
#     else:
#         if (size % 3) % 2 == 0:
#             ans += size // 3 * 2 + 1
#         else:
#             ans += size // 3 * 2 - 1

# print(ans)

# # 모범답안
# # 변수 선언 및 입력
# n = int(input())
# blocks = list(map(int, input().split()))


# # 생각해 보면, 그룹의 숫자를 고를 때 어느 숫자를 고르던
# # 그 숫자의 홀짝이 같다면 그룹의 총합에서 홀짝도 같아지게 됩니다.
# # 따라서 어느 숫자를 골랐는지 알 필요가 없으며, 짝수와 홀수 중 어느 숫자를
# # 새로 골랐는지만 정보를 가지고 있다면 문제를 풀 수 있습니다.
# even = 0
# odd = 0
# for block in blocks:
#     if(block % 2 == 0):
#         even += 1
#     else:
#         odd += 1

# # 그룹을 나눌때 숫자를 가능한 적게 쓰는 것이 유리합니다. 숫자를 적게 사용해야
# # 남은 숫자들로 더 많은 그룹을 만들 가능성이 생기기 때문입니다.

# # 생각해보면, 홀수 그룹을 만들 때 짝수 숫자를 그룹에 넣는것은 의미가 없습니다.
# # 짝수 숫자를 넣으나 마나 어차피 그룹의 홀짝성이 변하지 않기 때문입니다.
# # 따라서 홀수 그룹을 만들 때에는 짝수 숫자를 넣지 않고 홀수 숫자만 1개로
# # 그룹을 형성하는 것이 유리합니다.
# # 짝수 그룹을 만들 때에는 홀수 2개로 만들거나 짝수 1개로 만들 수 있는데,
# # 홀수 그룹을 만들 때에 사용되지 않는 짝수 숫자부터 그룹에 이용하는 것이 유리합니다.

# group_num = 0
# while True:
#     # 묶음을 짝수, 홀수를 번갈아가며 나오게끔 해야 하므로
#     # group_num이 짝수일 때, 묶음은 짝수로 만들어야 하고
#     # group_num이 홀수일 때, 묶음은 홀수로 만들어야 합니다.

#     if group_num % 2 == 0:
#         # 짝수 묶음을 만들 때에는, 짝수 숫자 1개로 그룹을 만드는 것이 최선입니다.
#         # 만약 짝수 숫자가 부족하다면, 홀수 숫자 2개로 그룹을 만드는 것이 최선입니다.
#         if even:
#             even -= 1
#             group_num += 1
#         elif odd >= 2:
#             odd -= 2
#             group_num += 1
#         else:
#             # 더 이상 그룹을 만들지 못하는 상황입니다.

#             # 아직 숫자가 남아있다면 남아 있는 숫자들로 짝수 그룹을 만들지 못합니다.
#             # 이 경우 ... + (짝수 그룹 A) + (홀수 그룹 B) + (나머지 C(홀수 그룹))
#             # 다음과 같은 상태인데, 무슨 짓을 해도 그룹의 개수를 늘리거나 유지해서는
#             # 문제 조건을 만족할 수 없습니다.

#             # 그 이유는 그룹의 개수를 늘리려면 ... + 짝수 그룹 + 홀수 그룹 + 짝수 그룹 형태가,
#             # 그룹의 개수를 유지하려면 ... + 짝수 그룹 + 홀수 그룹 형태가 되어야만 하는데
#             # 홀짝성을 생각해 보았을 때 이는 불가능합니다.
#             # 따라서 그룹의 개수를 1개 줄이는
#             # ... + 짝수 그룹(A + B + C) 형태가 최선입니다.
#             if even > 0 or odd > 0:
#                 group_num -= 1

#             break

#     else:
#         # 홀수 묶음을 만들 때에는, 홀수 숫자 1개로 그룹을 만드는 것이 최선입니다.
#         # 짝수 숫자만으로는 홀수 묶음을 만들 수 없습니다.
#         if odd:
#             odd -= 1
#             group_num += 1
#         else:
#             # 더 이상 그룹을 만들지 못하는 상황입니다.

#             # 아직 숫자가 남아있다면 남아 있는 숫자들로 홀수 그룹을 만들지 못합니다.
#             # 이 경우 ... + (홀수 그룹 A) + (짝수 그룹 B) + (나머지 C(짝수 그룹))
#             # 다음과 같은 상태인데, 무슨 짓을 해도 그룹의 개수를 늘리는 방식으로는
#             # 문제 조건을 만족할 수 없습니다.

#             # 그 이유는 그룹의 개수를 늘리려면 ... + 홀수 그룹 + 짝수 그룹 + 홀수 그룹 형태가
#             # 되어야만 하는데 홀짝성을 생각해 보았을 때 이는 불가능합니다.
#             # 따라서 그룹의 개수를 유지하는
#             # ... + (홀수 그룹 A) + (짝수 그룹 (B + C)) 형태가 최선입니다.

#             break

# print(group_num)