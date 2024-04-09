Y, M, D = map(int, input().split())

def is_leap_year(y):
    if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0:
        return True
    
    return False

def is_wrong_day(y, m, d):
    if m in [4, 6, 9, 11] and d > 30:
        return True
    elif m == 2 and is_leap_year(y) and d > 29:
        return True
    elif m == 2 and is_leap_year(y) == False and d > 28:
        return True
    else:
        return False

if is_wrong_day(Y, M, D):
    print(-1)
else:
    if M in [12, 1, 2]:
        print("Winter")
    elif M in [3, 4, 5]:
        print("Spring")
    elif M in [6, 7, 8]:
        print("Summer")
    elif M in [9, 10, 11]:
        print("Fall")
    else:
        print(-1)

# # 모범 답안
# y, m, d = tuple(map(int, input().split()))


# def is_leap_year(y):
#     # 4의 배수가 아니라면 윤년이 확실히 아닙니다.
#     if y % 4 != 0:
#         return False
    
#     # 여기까지 온 이상 4의 배수임을 가정해도 됩니다.
#     # 그 중 100의 배수가 아니라면 확실히 윤년입니다.
#     if y % 100 != 0:
#         return True
    
#     # 여기까지 온 이상 100의 배수임을 가정해도 됩니다.
#     # 그 중 400의 배수라면 확실히 윤년입니다.
#     if y % 400 == 0:
#         return True
    
#     # 여기까지 온 이상 100의 배수이지만, 400의 배수가 아닙니다.
#     # 따라서 확실히 윤년이 아닙니다.
#     return False


# def is_exist_day(y, m, d):
#     #                  1. 2.  3. 4.  5    6.  7.  8.  9. 10. 11  12
#     num_of_days = [0, 31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

#     # 윤년에 대한 처리를 진행합니다.
#     num_of_days[2] = 29 if is_leap_year(y) else 28

#     # d가 해당 월의 최대 일 수를 넘지 않아야 합니다.
#     return d <= num_of_days[m]

   
# # y년 m월 d일이 존재하지 않는다면 -1을 출력합니다.
# if not is_exist_day(y, m, d):
#     print(-1)
# else:
#     # y년 m월 d일이 존재한다면 달에 맞는 계절을 출력합니다.
#     if 3 <= m and m <= 5:
#         print("Spring")
#     elif 6 <= m and m <= 8:
#         print("Summer")
#     elif 9 <= m and m <= 11:
#         print("Fall")
#     else:
#         print("Winter")