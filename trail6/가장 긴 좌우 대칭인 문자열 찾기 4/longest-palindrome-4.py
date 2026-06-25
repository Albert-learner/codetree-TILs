str = input()

# Please write your code here.
n = len(str)
answer = 1

for center in range(n):
    left = center
    right = center

    while left >= 0 and right < n and str[left] == str[right]:
        answer = max(answer, right - left + 1)
        left -= 1
        right += 1

    left = center
    right = center + 1

    while left >= 0 and right < n and str[left] == str[right]:
        answer = max(answer, right - left + 1)
        left -= 1
        right += 1

print(answer)