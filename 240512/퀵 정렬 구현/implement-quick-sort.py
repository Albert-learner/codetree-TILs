N = int(input())
n_lst = list(map(int, input().split()))

def quick_sort(lst):
    if len(lst) <= 1:
        return lst

    pivot = lst[len(lst) // 2]
    lesser_lst, equal_lst, greater_lst = [], [], []
    for n in lst:
        if n < pivot:
            lesser_lst.append(n)
        elif n > pivot:
            greater_lst.append(n)
        else:
            equal_lst.append(n)

    return quick_sort(lesser_lst) + equal_lst + quick_sort(greater_lst)

print(*quick_sort(n_lst))