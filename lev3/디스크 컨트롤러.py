def solution(jobs):
    jobs.sort(key=lambda x: (x[0], x[1]), reverse=True)
    print(f"jobs: {jobs}")
    waiting_job = [jobs.pop()]
    ans = 0
    finished = waiting_job[0][0]
    idx = 1
    while waiting_job or jobs:
        print(f"before waiting: {waiting_job}")
        start, running_time = waiting_job.pop()
        finished += running_time
        ans += (finished - start)
        print(f"finished: {finished}, ans: {ans}")

        cnt = 0
        for job in jobs[idx:]:
            if job[0] <= finished:
                waiting_job.append(job)
                cnt += 1
            else:
                break
        idx += cnt
        waiting_job.sort(key=lambda x: x[1], reverse=True)
        print(f"after waiting: {waiting_job}")
    return ans // len(jobs)


# print(solution([[0, 3], [1, 9], [2, 6]]))   # 9
# print(solution([[0, 5], [0, 4]]))   # 6
print(solution([[0, 5], [4, 1], [5, 1], [6, 1]]))   # 2
