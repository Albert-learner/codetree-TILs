n = int(input())
a = list(map(int, input().split()))

m = int(input())
b = list(map(int, input().split()))

# Please write your code here.
a_set = set(a)
b_set = set(b)

for num in b:
    print(1 if num in a_set else 0)