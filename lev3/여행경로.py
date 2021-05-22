"""
문제 설명
주어진 항공권을 모두 이용하여 여행경로를 짜려고 합니다. 항상 "ICN" 공항에서 출발합니다.
항공권 정보가 담긴 2차원 배열 tickets가 매개변수로 주어질 때, 방문하는 공항 경로를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
모든 공항은 알파벳 대문자 3글자로 이루어집니다.
주어진 공항 수는 3개 이상 10,000개 이하입니다.
tickets의 각 행 [a, b]는 a 공항에서 b 공항으로 가는 항공권이 있다는 의미입니다.
주어진 항공권은 모두 사용해야 합니다.
만일 가능한 경로가 2개 이상일 경우 알파벳 순서가 앞서는 경로를 return 합니다.
모든 도시를 방문할 수 없는 경우는 주어지지 않습니다.

입출력 예
tickets	                                                                        return
[["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	                            ["ICN", "JFK", "HND", "IAD"]
[["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]	["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]

입출력 예 설명
예제 #1
["ICN", "JFK", "HND", "IAD"] 순으로 방문할 수 있습니다.

예제 #2
["ICN", "SFO", "ATL", "ICN", "ATL", "SFO"] 순으로 방문할 수도 있지만
["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"] 가 알파벳 순으로 앞섭니다.
"""


def solution(tickets):
    paths = {}
    for t in tickets:
        if t[0] not in paths:
            paths[t[0]] = list()
        paths[t[0]].append(t[1])
    for k in paths:
        paths[k].sort(reverse=True)
    # pointer = {k: 0 for k in paths}
    #
    # def dfs(paths, answer, pointer, cnt, N):
    #     if cnt == N:
    #         return True, answer
    #     k = answer[-1]
    #     if k in paths:
    #         idx = pointer[k]
    #         if paths[k][idx] in answer:
    #             pointer[paths[k][idx]] += 1
    #         while 1:
    #             flag, ans = dfs(paths, answer + [paths[k][idx]], pointer, cnt+1, N)
    #             if len(paths[k]) >= 2 and not flag:
    #                 temp = paths[k][idx]
    #                 paths[k][idx] = paths[k][idx+1]
    #                 paths[k][idx+1] = temp
    #             elif flag:
    #                 break
    #             else:
    #                 return False, answer[:-1]
    #         return True, ans
    #     return False, answer[:-1]
    #
    # N = len(tickets)+1
    # _, path = dfs(paths, ["ICN"], pointer, 1, N)
    # return path

    # 접근 방법 참고
    stack = ["ICN"]
    answer = []
    while stack:
        top = stack[-1]
        if top not in paths or not paths[top]:
            answer.append(stack.pop())
        else:
            stack.append(paths[top].pop())
    return answer[::-1]

# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))   # ["ICN", "JFK", "HND", "IAD"]
# print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))    # ["ICN", "ATL", "ICN", "SFO", "ATL", "SFO"]
# print(solution([["ICN", "AAA"], ["AAA", "BBB"], ["AAA", "CCC"], ["BBB", "DDD"], ["CCC", "AAA"], ["DDD", "CCC"]])) # ['ICN', 'AAA', 'BBB', 'DDD', 'CCC', 'AAA', 'CCC']
# print(solution([["ICN", "AAA"], ["ICN", "AAA"], ["ICN", "AAA"], ["AAA", "ICN"], ["AAA", "ICN"]])) # ['ICN', 'AAA', 'ICN', 'AAA', 'ICN', 'AAA']
print(solution([["ICN", "AAA"], ["AAA", "BBB"], ["AAA", "CCC"], ["BBB", "DDD"], ["CCC", "AAA"]]))   # ['ICN', 'AAA', 'CCC', 'AAA', 'BBB', 'DDD']
