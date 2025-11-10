n, m = map(int, input().split())
nums = list(map(int, input().split()))

# Please write your code here.
start_map = {}  
end_map = {}  

def add_interval(s, e):
    start_map[s] = e
    end_map[e] = s

def remove_interval(s, e):
    start_map.pop(s, None)
    end_map.pop(e, None)

removed_sorted = sorted(nums)
prev = -1
max_len = 0

first = 0
for r in removed_sorted:
    if first <= r - 1:
        add_interval(first, r - 1)
        max_len = max(max_len, r - 1 - first + 1)
    first = r + 1
if first <= n:
    add_interval(first, n)
    max_len = max(max_len, n - first + 1)

rev_ans = [max_len]

for x in reversed(nums):
    left_start = end_map.get(x - 1, None)
    right_end = start_map.get(x + 1, None)

    if left_start is None and right_end is None:
        add_interval(x, x)
        new_len = 1
    elif left_start is not None and right_end is None:
        left_end = x - 1
        remove_interval(left_start, left_end)
        add_interval(left_start, x)
        new_len = x - left_start + 1
    elif left_start is None and right_end is not None:
        right_start = x + 1
        remove_interval(right_start, right_end)
        add_interval(x, right_end)
        new_len = right_end - x + 1
    else:
        left_end = x - 1
        right_start = x + 1
        remove_interval(left_start, left_end)
        remove_interval(right_start, right_end)
        add_interval(left_start, right_end)
        new_len = right_end - left_start + 1

    if new_len > max_len:
        max_len = new_len
    rev_ans.append(max_len)

for i in range(1, m + 1):
    print(rev_ans[m - i])