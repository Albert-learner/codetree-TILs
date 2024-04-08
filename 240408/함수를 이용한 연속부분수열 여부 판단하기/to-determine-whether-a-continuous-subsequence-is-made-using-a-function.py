n1, n2 = map(int, input().split())
a_seq = list(map(int, input().split()))
b_seq = list(map(int, input().split()))

if all(elem in a_seq for elem in b_seq):
    print("Yes")
else:
    print("No")