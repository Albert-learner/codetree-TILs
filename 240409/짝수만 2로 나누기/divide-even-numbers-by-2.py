N = int(input())
n_lst = list(map(int, input().split()))

def modify(lst):
    for n_idx, n in enumerate(lst):
        if n % 2 == 0:
            lst[n_idx] = n // 2
    
    return lst

print(*modify(n_lst))