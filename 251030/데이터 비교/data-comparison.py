n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

# Please write your code here.
arr1_set = set(arr1)

for num in arr2:
    print(1 if num in arr1_set else 0, end = ' ')