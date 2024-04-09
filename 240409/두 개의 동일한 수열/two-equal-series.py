N = int(input())
a_seq = list(map(int, input().split()))
b_seq = list(map(int, input().split()))

a_seq.sort()
b_seq.sort()

print("Yes" if a_seq == b_seq else "No")