n = int(input())

# Please write your code here.
import sys
sys.setrecursionlimit(10 ** 6)

digits = ['4', '5', '6']
ans_found = False

def is_good(s: str) -> bool:
    L = len(s)
    for l in range(1, L // 2 + 1):
        if s[-l:] == s[-2 * l:-l]:
            return False
    return True

def dfs(s: str):
    global ans_found
    if ans_found:
        return
    if len(s) == n:
        print(s)
        ans_found = True
        return
    for d in digits:
        ns = s + d
        if is_good(ns):
            dfs(ns)
            if ans_found:
                return

dfs("")