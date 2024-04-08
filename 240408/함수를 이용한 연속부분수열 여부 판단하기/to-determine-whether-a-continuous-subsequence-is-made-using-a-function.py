n1, n2 = map(int, input().split())
a_seq = list(map(int, input().split()))
b_seq = list(map(int, input().split()))

for b in b_seq:
    if b not in a_seq:
        print("No")
        break

print("Yes")