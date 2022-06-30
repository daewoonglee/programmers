def solution(a):
    if len(a) < 3: return len(a)
    ans = 2
    l, r = a[0], min(a[2:])
    for i, n in enumerate(a[1:-1]):
        print(f"n: {n}, left: {l}, right: {r}")
        if l < n and r < n: continue
        ans += 1
        l = a[i+1] if a[i+1] < l else l
        r = min(a[i+2:]) if a[i+1] == r else r
    return ans


print(solution([9,-1,-5])) # 3
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33])) # 6

