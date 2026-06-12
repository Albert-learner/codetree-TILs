n = int(input())
sequences = [input().strip() for _ in range(n)]

# Please write your code here.
sequences.sort()

for i in range(n - 1):
    if sequences[i] != sequences[i + 1] and sequences[i + 1].startswith(sequences[i]):
        print(0)
        break
else:
    print(1)