import bisect

n = int(input())
matters = []
for i in range(n):
    p, l = map(int, input().split())
    bisect.insort(matters, (l, p))
m = int(input())
for i in range(m):
    function = list(map(str, input().split()))
    if function[0] == "ad":  
        bisect.insort(matters, (int(function[2]), int(function[1])))
    elif function[0] == "sv": 
        matters.remove((int(function[2]), int(function[1])))
    else:  
        x = int(function[1])
        print(matters[0][1]) if x == -1 else print(matters[-1][1])