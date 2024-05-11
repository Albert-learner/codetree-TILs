N = int(input())
n_lst = list(map(int, input().split()))

def merge_sort(lst):
    if len(lst) < 2:
        return lst

    mid = len(lst) // 2
    low_lst = merge_sort(lst[:mid])
    high_lst = merge_sort(lst[mid:])

    merge_lst = []
    l, h = 0, 0
    while l < len(low_lst) and h < len(high_lst):
        if low_lst[l] < high_lst[h]:
            merge_lst.append(low_lst[l])
            l += 1
        else:
            merge_lst.append(high_lst[h])
            h += 1

    merge_lst += low_lst[l:]
    merge_lst += high_lst[h:]

    return merge_lst

print(*merge_sort(n_lst))