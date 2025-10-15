s = input()
p = input()

# Please write your code here.
import re

print("true" if re.fullmatch(p, s) else "false")