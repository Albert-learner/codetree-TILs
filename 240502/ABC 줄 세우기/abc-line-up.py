N = int(input())
line = input().split()

def bubble_sort(lst):
    cnts = 0
    for i in range(len(lst) - 1, 0, -1):
        for j in range(i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                cnts += 1

    return cnts, lst

total_cnts, sort_line = bubble_sort(line)
print(total_cnts)