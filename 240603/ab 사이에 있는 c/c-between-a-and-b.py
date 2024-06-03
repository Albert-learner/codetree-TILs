a, b, c = map(int, input().split())

answer = ""
for n in range(a, b + 1):
    if n % c == 0:
        answer += "YES"
        break
    

if answer != "YES":
    answer = "NO"
print(answer)