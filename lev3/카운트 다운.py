def solution(target):
    ans = [0, 0]
    q,d = 1668, target
    if target > 70:
        # 17(51), 18(54), 19(57), 20(60), 50(bull)
        for x in [60, 57, 54, 51, 50]:
            xq, xd = divmod(target, x)
            print(x, xq, xd)
            if xq < q:
                q = xq
                d = xd
                ans = [q, q] if x == 50 else [q, 0]
                if d == 0: return ans
            else:
                if x == 50 and xd == 0 and xq-1 == q:
                    return [xq, xq]
    elif 50 < target <= 70:
        return [2, 2]
    elif target == 50:
        return [1, 1]

    if d <= 20:
        ans[0] += 1
        ans[1] += 1
    elif d % 3 == 0 or (d <= 40 and d % 2 == 0):
        ans[0] += 1
    elif d > 40:
        ans[0] += 2
        ans[1] += 1
    else:
        ans[0] += 2
        ans[1] += 2
    return ans


# print(solution(21)) # [1,0]
# print(solution(58)) # [2,2]
# print(solution(100000)) # [1667, 0]
# print(solution(1)) # [1,1]
print(solution(35)) #[2,2]
print(solution(49)) #[2,1]
print(solution(40)) #[1,0]
print(solution(41)) #[2,1]
print(solution(47)) #[2,1]
# print(solution(180)) #[3,0]
# print(solution(250))
# print(solution(50)) # [1,1]
print(solution(37)) # [2,2]
