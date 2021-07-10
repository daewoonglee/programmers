def solution(jobs):
    N = len(jobs)
    jobs.sort(key=lambda x: (x[0], x[1]), reverse=True)
    print(f"jobs: {jobs}")
    waiting_job = [jobs.pop()]
    ans = 0
    moved = waiting_job[0][0]

    while waiting_job:
        print(f"before waiting: {waiting_job}")
        start, running_time = waiting_job.pop()
        moved += running_time
        ans += (moved - start)
        print(f"moved: {moved}, ans: {ans}")

        while jobs and jobs[-1][0] <= moved:
            waiting_job.append(jobs.pop())

        if waiting_job:
            waiting_job.sort(key=lambda x: x[1], reverse=True)
        elif jobs:
            waiting_job = [jobs.pop()]
            moved = waiting_job[0][0]
        print(f"after waiting: {waiting_job}")
    return ans // N


# print(solution([[0, 3], [1, 9], [2, 6]]))   # 9
# print(solution([[0, 5], [0, 4]]))   # 6
print(solution([[0, 5], [0, 4], [0, 4]]))   # 8
# print(solution([[0, 5], [4, 1], [5, 1], [6, 1]]))   # 2
# print(solution([[1, 3], [5, 2]]))   # 2
