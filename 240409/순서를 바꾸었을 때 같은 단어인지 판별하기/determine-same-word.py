first = input()
second = input()

first_str = "".join(sorted(list(first)))
second_str = "".join(sorted(list(second)))
print("Yes" if first_str == second_str else "No")