def solution(gems):
    """
    def shopping_gems():
        shopping_gem_dict = dict()
        shopping_idx = 0
        for i, gem in enumerate(gem_list[::-1]):
            if gem not in shopping_gem_dict:
                shopping_gem_dict[gem] = 1
            if len(shopping_gem_dict) == total_gem_list:
                shopping_idx = i
                break
        return [len(gem_list)-shopping_idx+step, len(gem_list)+step]

    def update_shopping_list():
        for g in gem_list[:shopping_list[0] - step]:
            if g in gem_dict:
                if gem_dict[g] > 1:
                    gem_dict[g] -= 1
                else:
                    del gem_dict[g]
        del gem_list[:shopping_list[0] - step]

    # 4.967148605999999
    ans = [0, 100000]
    N = len(gems)
    total_gem_list = len(set(gems))

    step = 0
    idx = 0
    gem_dict = dict()
    gem_list = list()
    while idx < N:
        g = gems[idx]
        if g not in gem_dict:
            gem_dict[g] = 1
        else:
            gem_dict[g] += 1
        gem_list.append(g)

        if len(gem_dict) == total_gem_list:
            shopping_list = shopping_gems()
            shopping_diff = shopping_list[-1] - shopping_list[0]
            ans_diff = ans[-1] - ans[0]
            if shopping_diff < ans_diff or (shopping_diff == ans_diff and shopping_list[0] < ans[0]):
                ans = shopping_list

            update_shopping_list()

            idx = shopping_list[-1]
            step = shopping_list[0]
        else:
            idx += 1

    return ans
    """
    # code refactoring - 4.472075382
    N = len(gems)
    gem_size = len(set(gems))
    dic = {gems[0]: 1}
    ans = [0, N]
    start, end = 0, 0
    while start < N and end < N:
        if len(dic) == gem_size:
            if end - start < ans[1] - ans[0]:
                ans = [start, end]
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            start += 1

        else:
            end += 1
            if end == N:
                break
            if gems[end] in dic.keys():
                dic[gems[end]] += 1
            else:
                dic[gems[end]] = 1

    return [ans[0] + 1, ans[1] + 1]


# print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])) #[3, 7]
# print(solution(["AA", "AB", "AC", "AA", "AC"])) # [1, 3]
# print(solution(["XYZ", "XYZ", "XYZ"])) # [1, 1]
# print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])) # [1, 5]
print(solution(["A", "A", "A", "B", "A", "A", "C", "B", "A", "A"])) # [6, 8]


if __name__ == "__main__":
    from timeit import Timer
    query = [
        ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"],
        ["AA", "AB", "AC", "AA", "AC"],
        ["XYZ", "XYZ", "XYZ"],
        ["ZZZ", "YYY", "NNNN", "YYY", "BBB"],
        ["A", "A", "A", "B", "A", "A", "C", "B", "A", "A"],
        ["A"*1000],
        [str(i) for i in range(1000)],
        ["1","2","3","4","5","5","6","6","7","8","9","10","9","1","2","3","4","1","2","3","8","9"]
    ]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=10000))
