n, m = map(int, input().split())
arr = list(map(int, input().split()))
query = list(map(int, input().split()))

# Please write your code here.
n_str = "".join(map(str, arr))
for qry in query:
    if str(qry) not in n_str:
        print(-1)
    else:
        print(n_str.find(str(qry)) + 1)