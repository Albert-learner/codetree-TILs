n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

# Please write your code here.
b_set = set(b)

for num in b_set:
    print(1 if num in a else 0)