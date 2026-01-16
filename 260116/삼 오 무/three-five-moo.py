n = int(input())

# Please write your code here.
idx = 1
nums_lst, digits_lst = [], []

while idx <= 10 ** 9:
    if idx % 3 == 0 or idx % 5 == 0:
        nums_lst.append("Moo")
    else:
        nums_lst.append(idx)

    if len(digits_lst) < n:
        if nums_lst[-1] != "Moo":
            digits_lst.append(idx)
    elif len(digits_lst) == n:
        print(digits_lst[-1])
        break

    idx += 1