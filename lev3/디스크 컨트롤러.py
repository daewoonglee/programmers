

def solution(jobs):
    # 0.170955303
    # N = len(jobs)
    # jobs.sort(key=lambda x: (x[0], x[1]), reverse=True)
    # waiting_job = [jobs.pop()]
    # ans = 0
    # moved = waiting_job[0][0]
    #
    # while waiting_job:
    #     start, running_time = waiting_job.pop()
    #     moved += running_time
    #     ans += (moved - start)
    #
    #     while jobs and jobs[-1][0] <= moved:
    #         waiting_job.append(jobs.pop())
    #
    #     if waiting_job:
    #         waiting_job.sort(key=lambda x: x[1], reverse=True)
    #     elif jobs:
    #         waiting_job = [jobs.pop()]
    #         moved = waiting_job[0][0]
    # return ans // N

    # code refactoring 02 - using priority queue, 0.20985568000000002
    import heapq
    from collections import deque

    tasks = deque(sorted([(x[1], x[0]) for x in jobs], key=lambda x: (x[1], x[0])))
    q = []
    heapq.heappush(q, tasks.popleft())
    current_time, total_response_time = 0, 0
    while len(q) > 0:
        dur, arr = heapq.heappop(q)
        current_time = max(current_time + dur, arr + dur)
        total_response_time += current_time - arr
        while len(tasks) > 0 and tasks[0][1] <= current_time:
            heapq.heappush(q, tasks.popleft())
        if len(tasks) > 0 and len(q) == 0:
            heapq.heappush(q, tasks.popleft())
    return total_response_time // len(jobs)


# print(solution([[0, 3], [1, 9], [2, 6]]))   # 9
# print(solution([[0, 5], [0, 4]]))   # 6
# print(solution([[0, 5], [0, 4], [0, 4]]))   # 8
print(solution([[0, 5], [4, 1], [5, 1], [6, 1]]))   # 2
# print(solution([[1, 3], [5, 2]]))   # 2


if __name__ == '__main__':
    from timeit import Timer
    query = [[[0, 3], [1, 9], [2, 6]],
             [[0, 5], [0, 4]],
             [[0, 5], [0, 4], [0, 4]],
             [[0, 5], [4, 1], [5, 1], [6, 1]],
             [[1, 3], [5, 2]]]
    t = Timer(f"for t in {query}: solution(t)", "from __main__ import solution")
    print(t.timeit(number=10000))
