def solution(k, d):
    ans = 0
    for x in range(0, d+1, k):
        for y in range(d//k+1, -1, -1):
            print(f"x: {x}, y: {y}, y': {y*k}, dist: {(x**2+y**2)**0.5}")
            if (x**2 + (y*k)**2)**0.5 <= d:
                ans += y + 1
                break
    return ans


print(solution(2, 4)) # 6
print(solution(1, 5)) # 26
print(solution(5, 9)) # 4

