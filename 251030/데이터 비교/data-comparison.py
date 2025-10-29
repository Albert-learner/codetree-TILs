n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

# Please write your code here.
for num in arr2:
    if num in arr1:
        print(1, end = ' ')
    else:
        print(0, end = ' ')