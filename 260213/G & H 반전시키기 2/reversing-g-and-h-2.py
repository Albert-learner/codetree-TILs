n = int(input())
a = input()
b = input()

# Please write your code here.
flip, ans = 0, 0

for i in range(n - 1, -1, -1):
    cur = a[i]
    if flip % 2 == 1:
        cur = 'H' if cur == 'G' else 'G'  

    if cur != b[i]:
        ans += 1
        flip ^= 1  

print(ans)