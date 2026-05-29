S = input()

# Please write your code here.
def manacher_odd(s):
    n = len(s)
    d = [0] * n
    l, r = 0, -1

    for i in range(n):
        k = 1 if i > r else min(d[l + r - i], r - i + 1)

        while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
            k += 1

        d[i] = k

        if i + k - 1 > r:
            l = i - k + 1
            r = i + k - 1

    return d

def manacher_even(s):
    n = len(s)
    d = [0] * n
    l, r = 0, -1

    for i in range(n):
        k = 0 if i > r else min(d[l + r - i + 1], r - i + 1)

        while i - k - 1 >= 0 and i + k < n and s[i - k - 1] == s[i + k]:
            k += 1

        d[i] = k

        if i + k - 1 > r:
            l = i - k
            r = i + k - 1

    return d

odd = manacher_odd(S)
even = manacher_even(S)

answer = sum(odd) + sum(even)
print(answer)