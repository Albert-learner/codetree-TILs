A = input()

def is_palindrome(a_str):
    if a_str == a_str[::-1]:
        return "Yes"
    else:
        return "No"

print(is_palindrome(A))