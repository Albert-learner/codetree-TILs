from collections import Counter

X, Y = map(int, input().split())
nums_lst = list(range(X, Y + 1))

def is_interest_num(num):
    cntr = Counter(str(num))

    if len(cntr) == 2 and (tuple(cntr.values()) == (sum(cntr.values()) - 1, 1) or tuple(cntr.values()) == (1, sum(cntr.values()) - 1)):
        return True
    else:
        return False


interest_nums = [num for num in nums_lst if is_interest_num(num)]
print(len(interest_nums))