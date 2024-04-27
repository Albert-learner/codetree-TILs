from itertools import combinations

num_lst = list(map(int, input().split()))
num_lst.sort()

def possible(x):
    a, b, c, d = x

    if (a + b in num_lst) and (b + c in num_lst) and (c + d in num_lst) and (d + a in num_lst) and \
       (a + c in num_lst) and (b + d in num_lst) and \
       (a + b + c in num_lst) and (a + b + d in num_lst) and (a + c + d in num_lst) and (b + c + d in num_lst) and \
       (a + b + c + d in num_lst):
       return True

    return False

combs_set = set(combinations(num_lst, 4))
for comb in combs_set:
    if possible(comb):
        for num in comb:
            print(num, end = " ")
        break

# # 모범답안
# MAX_A = 40
# MAX_N = 15

# # 변수 선언 및 입력
# arr = list(map(int, input().split()))
    
# # 모든 a, b, c, d를 확인해서
# # 이 합들이 arr과 같은지 여부를 확인합니다.
# for a in range(1, MAX_A + 1):
#     for b in range(a, MAX_A + 1):
#         for c in range(b, MAX_A + 1):
#             for d in range(c, MAX_A + 1):
#                 arr2 = [a, b, c, d, a + b, b + c, c + d, d + a,
#                     a + c, b + d, a + b + c, a + b + d, a + c + d, b + c + d,
#                     a + b + c + d]
                
#                 if sorted(arr) == sorted(arr2):
#                     # 만약 두 배열이 완전히 같다면 a, b, c, d조합을 찾아냈습니다.
#                     print(a, b, c, d)