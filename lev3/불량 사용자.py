from itertools import permutations, product


def solution(user_id, banned_id):
    # # 0.30337167300000006
    # def is_matched(val):
    #     for i, bid in enumerate(banned_id):
    #         if visited[i] or len(bid) != len(val):
    #             continue
    #         for b, v in zip(bid, val):
    #             if b != "*" and b != v:
    #                 break
    #         else:
    #             visited[i] = 1
    #             return True
    #     return False
    #
    # N = len(banned_id)
    # permutation_list = permutations(user_id, N)
    # ans = set()
    # for values in permutation_list:
    #     visited = [0] * N
    #     for value in values:
    #         if not is_matched(value):
    #             break
    #     else:
    #         ans.add(tuple(sorted(list(values))))
    #
    # return len(ans)

    # 0.096853074
    def dfs(idx, temp):
        global ans

        if len(temp) == len(matching_id):
            ans.add(tuple(sorted(temp)))
            return 0

        for mid in matching_id[idx]:
            if mid not in temp:
                temp.append(mid)
                print(f"before temp: {temp},  mid: {mid}")
                dfs(idx+1, temp)
                temp.pop()
                print(f"after temp: {temp}, mid: {mid}")

    def is_matched(str1, str2):
        if len(str1) != len(str2):
            return False
        for s1, s2 in zip(str1, str2):
            if s1 != "*" and s1 != s2:
                return False
        return True

    global ans
    ans = set()
    matching_id = {}
    for i, bid in enumerate(banned_id):
        for j, uid in enumerate(user_id):
            if is_matched(bid, uid):
                if i not in matching_id:
                    matching_id[i] = set()
                matching_id[i].add(j)
    print(matching_id)

    dfs(0, [])
    # print(ans)
    return len(ans)


# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"])) # 2
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])) # 2
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])) # 3
# print(solution(["frodo", "fradi", "crodo", "abc456", "def456", "efg456","abc123", "frodoc"], ["*rodo", "*rodo", "***456", "******"])) # 9
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*****", "*****", "*****", "******", "******"])) # 1
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*****"])) # 3
# print(solution(["frodo1", "fradi1", "crodo1", "abc123", "frodoc"], ["******", "******"])) # 10
# print(solution(["a", "b", "c", "d", "e", "f", "g", "h"], ["*", "*", "*", "*", "*", "*", "*", "*"])) # 1


# if __name__ == "__main__":
#     from timeit import Timer
#     query = [
#         [["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]],
#         [["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]],
#         [["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"]],
#         [["frodo", "fradi", "crodo", "abc456", "def456", "efg456","abc123", "frodoc"], ["*rodo", "*rodo", "***456", "******"]],
#         [["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*****", "*****", "*****", "******", "******"]],
#         [["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*****"]],
#         [["frodo1", "fradi1", "crodo1", "abc123", "frodoc"], ["******", "******"]],
#         [["a", "b", "c", "d", "e", "f", "g", "h"], ["*", "*", "*", "*", "*", "*", "*", "*"]]
#     ]
#     t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
#     print(t.timeit(number=1))
