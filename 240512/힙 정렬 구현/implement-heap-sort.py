N = int(input())
n_lst = list(map(int, input().split()))

def heapify(lst, lst_len):
    last_parent = lst_len // 2 - 1
    for cur in range(last_parent, -1, -1):
        while cur <= last_parent:
            child = cur * 2 + 1
            sibling = child + 1
            if sibling < lst_len and lst[child] < lst[sibling]:
                child = sibling
            if lst[cur] < lst[child]:
                lst[cur], lst[child] = lst[child], lst[cur]
                cur = child
            else:
                break
    
def heap_sort(lst):
    for lst_len in range(len(lst), 1, -1):
        heapify(lst, lst_len)
        lst[lst_len - 1], lst[0] = lst[0], lst[lst_len - 1]

heap_sort(n_lst)
print(*n_lst)