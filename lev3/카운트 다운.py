import sys
sys.setrecursionlimit(10000)


def solution(target):
    def countdown(n, q, m):
        if n == 0: return [q, m]
        elif n > 20 and (n % 3 == 0 or (n <= 40 and n % 2 == 0)): return [q+1, m]
        elif n == 50 or n <= 20: return [q+1, m+1]
        elif n > 50 or n < 40: return [q+2, m+2]
        else: return [q+2, m+1]

    def search(depth, search_list):
        global ans
        for x in [51, 54, 57, 60]:
            search_list[depth] = x
            d = target - sum(search_list)
            darts, min_times = countdown(d, q, q-(depth+1))
            # print(f"x: {x}, d: {d}, cnt: {darts}, {min_times}, list: {search_list}, ans: {ans}")
            if ans[0] >= darts:
                if ans[0] == darts and ans[1] < min_times:
                    ans = [darts, min_times]
                elif ans[0] > darts:
                    ans = [darts, min_times]
            if depth+1 < q:
                search(depth+1, search_list[:])

    global ans
    q, d = divmod(target, 50)
    target_list = [50] * q
    ans = countdown(d, q, q)
    if q:
        search(0, target_list[:])
    return ans


# print(solution(21)) # [1,0]
# print(solution(58)) # [2,2]
# print(solution(100000)) # [1667, 0]
# print(solution(1)) # [1,1]
# print(solution(35)) #[2,2]
# print(solution(49)) #[2,1]
# print(solution(40)) #[1,0]
# print(solution(41)) #[2,1]
# print(solution(47)) #[2,1]
# print(solution(180)) #[3,0]
# print(solution(250)) #[5,5]
# print(solution(103)) # [3,3]
# print(solution(102)) # [2,0]
# print(solution(101)) # [2,1]
# print(solution(117)) # [2,0]
print(solution(160)) # [3,2]
# print(solution(147)) # [4,3]
# print(solution(191)) # [4,2]
# print(solution(247)) # [4,2]
# 141, 147 -> 3, 1
# 191, 197 -> 4, 2
# 241, 247 -> 5, 3
# print(solution(37)) # [2,2]
