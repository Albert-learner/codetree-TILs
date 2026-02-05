n = int(input())
arr = [input().strip() for _ in range(n)]

# Please write your code here.
from functools import cmp_to_key

def compare(x: str, y: str) -> int:
    if x + y > y + x:
        return -1
    if x + y < y + x:
        return 1
    return 0

arr.sort(key = cmp_to_key(compare))

if arr[0] == "0":
    print("0")
else:
    print("".join(arr))