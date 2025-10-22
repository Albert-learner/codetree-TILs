n, k = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
arr.sort()
ans = 0
for i in range(n - 2):
    l, r = i + 1, n - 1
    while l < r:
        s = arr[i] + arr[l] + arr[r]
        if s == k:
            if arr[l] != arr[r]:
                vL, vR = arr[l], arr[r]
                cntL = 1
                while l + cntL < r and arr[l + cntL] == vL:
                    cntL += 1
                cntR = 1
                while r - cntR > l and arr[r - cntR] == vR:
                    cntR += 1
                ans += cntL *cntR
                l += cntL
                r -= cntR
            else:
                m = r - l + 1
                ans += m * (m - 1) // 2
                break

        elif s < k:
            l += 1
        else:
            r -= 1

print(ans)