from collections import deque


def solution(picks, minerals):
    def remove_picks(picks_list):
        # 탐색 전 필요없는 곡괭이 제거
        q = N // 5 if N % 5 == 0 else N // 5 + 1
        if q < sum(picks_list):
            for _ in range(sum(picks_list) - q):
                idx = len(picks_list) - 1
                while 1:
                    if picks_list[idx] > 0:
                        picks_list[idx] -= 1
                        break
                    else:
                        idx -= 1
        return picks_list

    def bfs(q):
        mineral_types = 3
        ans = 25 * 50
        while q:
            picks_list, total, idx = q.popleft()
            print(f"p: {picks_list}, total: {total}, idx: {idx}")
            if (idx > N or sum(picks_list) <= 0) and ans > total:
                ans = total
            else:
                mineral_sum = [0] * mineral_types # diamond, iron, stone
                for mineral in minerals[idx: idx+5]:
                    for i in range(mineral_types):
                        mineral_sum[i] += dig[i][mineral]

                for i, pick in enumerate(picks_list):
                    if pick > 0:
                        picks_list[i] -= 1
                        q.append([[*picks_list], total+mineral_sum[i], idx+5])
                        picks_list[i] += 1
        return ans

    N = len(minerals)
    dig = {
        0: {"diamond": 1, "iron": 1, "stone": 1},
        1: {"diamond": 5, "iron": 1, "stone": 1},
        2: {"diamond": 25, "iron": 5, "stone": 1}
    }
    picks = remove_picks(picks)
    ans = bfs(deque([[picks, 0, 0]]))
    return ans


"""
모든 구간에서 5 구간씩 탐색하며 picks에서 사용할 수 있는 곡괭이로 경우의 수 계산
이를 반복 picks is null or minerals null
최소 점수 반환

        dia     iron    stone
dia     1       1       1
iron    5       1       1
stone   25      5       1
"""


# print(solution([1, 3, 2], ["diamond", "diamond", "diamond", "iron", "iron", "diamond", "iron", "stone"])) #12
# print(solution([0, 1, 1], ["diamond", "diamond", "diamond", "diamond", "diamond", "iron", "iron", "iron", "iron", "iron", "diamond"])) #50
# print(solution([1, 2, 3], ["diamond", "iron", "stone", "iron", "iron", "diamond", "diamond", "iron", "stone", "stone", "stone", "stone"])) #16
# print(solution([0, 1, 1], ["diamond", "iron", "iron", "iron", "iron", "diamond", "diamond", "stone", "stone", "stone"])) #58
# print(solution([0, 1, 3], ["stone", "stone", "stone", "stone", "iron", "iron", "iron"])) # 11
# print(solution([0, 1, 0], ["stone", "stone", "stone", "stone", "stone"])) # 5
# print(solution([0, 1, 5], ["stone"]*50)) # 155 diamond(1)*5 + iron(5)*25 + stone(4)*125, 30
print(solution([1, 1, 0], ["iron", "iron", "diamond", "iron", "stone", "diamond", "diamond", "diamond"])) # 12
