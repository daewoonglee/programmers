"""
문제 설명
n명이 입국심사를 위해 줄을 서서 기다리고 있습니다. 각 입국심사대에 있는 심사관마다 심사하는데 걸리는 시간은 다릅니다.
처음에 모든 심사대는 비어있습니다. 한 심사대에서는 동시에 한 명만 심사를 할 수 있습니다.
가장 앞에 서 있는 사람은 비어 있는 심사대로 가서 심사를 받을 수 있습니다. 하지만 더 빨리 끝나는 심사대가 있으면 기다렸다가 그곳으로 가서 심사를 받을 수도 있습니다.

모든 사람이 심사를 받는데 걸리는 시간을 최소로 하고 싶습니다.

입국심사를 기다리는 사람 수 n, 각 심사관이 한 명을 심사하는데 걸리는 시간이 담긴 배열 times가 매개변수로 주어질 때,
모든 사람이 심사를 받는데 걸리는 시간의 최솟값을 return 하도록 solution 함수를 작성해주세요.

제한사항
입국심사를 기다리는 사람은 1명 이상 1,000,000,000명 이하입니다.
각 심사관이 한 명을 심사하는데 걸리는 시간은 1분 이상 1,000,000,000분 이하입니다.
심사관은 1명 이상 100,000명 이하입니다.

입출력 예
n	times	return
6	[7, 10]	28

입출력 예 설명
가장 첫 두 사람은 바로 심사를 받으러 갑니다.
7분이 되었을 때, 첫 번째 심사대가 비고 3번째 사람이 심사를 받습니다.
10분이 되었을 때, 두 번째 심사대가 비고 4번째 사람이 심사를 받습니다.
14분이 되었을 때, 첫 번째 심사대가 비고 5번째 사람이 심사를 받습니다.
20분이 되었을 때, 두 번째 심사대가 비지만 6번째 사람이 그곳에서 심사를 받지 않고 1분을 더 기다린 후에 첫 번째 심사대에서 심사를 받으면 28분에 모든 사람의 심사가 끝납니다.

출처
※ 공지 - 2019년 9월 4일 문제에 새로운 테스트 케이스를 추가하였습니다. 도움을 주신 weaver9651 님께 감사드립니다.
"""


def solution(n, times):
    # time limited - 2.4755566300000003
    # times.sort()
    # run_times = [0 for _ in times]
    # next_times = [t for t in times]
    # for _ in range(n):
    #     idx = next_times.index(min(next_times))
    #     run_times[idx] = next_times[idx]
    #     next_times[idx] += times[idx]
    # # print(run_times)
    # return max(run_times)

    # 0.514366909
    min_time, max_time = 0, max(times) * n
    ans = max_time
    while min_time <= max_time:
        mid_time = (min_time + max_time) // 2
        person = sum([mid_time // t for t in times])
        if person >= n:
            max_time = mid_time - 1
            ans = mid_time
        elif person < n:
            min_time = mid_time + 1
    return ans


print(solution(6, [7, 10]))         # 28
print(solution(10, [7, 10, 5]))     # 25
print(solution(6, [1, 10]))         # 6
print(solution(6, [100, 1, 1]))     # 3
print(solution(100, [1 for _ in range(100)]))     # 1


if __name__ == '__main__':
    from timeit import Timer
    query = [[6, [7, 10]],
             [10, [7, 10, 5]],
             [6, [100, 1, 1]],
             [100, [1 for _ in range(100)]]]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))
