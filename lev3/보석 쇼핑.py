def solution(gems):
    def shopping_gems():
        shopping_N = len(gem_list)
        shopping_gem_dict = dict()
        li = []
        for i, gem in enumerate(gem_list[::-1]):
            if gem not in shopping_gem_dict:
                shopping_gem_dict[gem] = 1
            if len(shopping_gem_dict) == total_gem_list:
                li.append(shopping_N-i+skip_N)
                li.append(shopping_N+skip_N)
                break
        return li

    ans = [0, 100000]
    N = len(gems)
    skip_N = 0
    total_gem_list = len(set(gems))
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
            if (shopping_list[-1] - shopping_list[0]) < (ans[-1] - ans[0]):
                ans = shopping_list
            elif (shopping_list[-1] - shopping_list[0]) == (ans[-1] - ans[0]) and shopping_list[0] < ans[0]:
                ans = shopping_list
            idx = shopping_list[0]
            skip_N = shopping_list[0]
            gem_dict = dict()
            gem_list = list()
        else:
            idx += 1

    return ans


"""
DP, O(nk)으로 풀어야 할 듯
1. 루프 진행하면서 전체 보석의 종류가 들어오는 구간 탐색
    - 전체 보석이 쌓인 경우의 리스트를 뒤에서부터 탐색
    - 맨 뒤에서부터 보석 종류 탐색하며 k개의 보석 종류가 다 탐색된 시점이 정답
    - 가장 적은 경우를 가지는 탐색 시점을 저장
2. 팀섹된 시점+1부터 1번 반복 
"""

# print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"])) #[3, 7]
# print(solution(["AA", "AB", "AC", "AA", "AC"])) # [1, 3]
# print(solution(["XYZ", "XYZ", "XYZ"])) # [1, 1]
# print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"])) # [1, 5]
print(solution(["A", "A", "A", "B", "A", "A", "C", "B", "A", "A"])) # [6, 8]
