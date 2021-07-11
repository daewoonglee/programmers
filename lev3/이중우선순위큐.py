import heapq


def solution(operations):
    # ans = []
    # for oper in operations:
    #     c, n = oper.split()
    #     # print(f"c: {c}, n: {n}, ans: {ans}")
    #     if c == "I":
    #         ans.append(int(n))
    #         ans.sort()
    #     elif ans:
    #         ans.pop() if n == "1" else ans.pop(0)
    # return [ans[-1], ans[0]] if ans else [0, 0]

    # code refactoring - using heapq
    res = []
    for oper in operations:
        cmd, v = oper.split(' ')
        print(res)
        if cmd == 'I':
            heapq.heappush(res, int(v))
        elif res:
            if v == "-1":
                print(f"-1 origin: {res}")
                heapq.heapify(res)
                print(f"-1 heapify: {res}")
                heapq.heappop(res)
            else:
                print("1")
                heapq._heapify_max(res)
                heapq._heappop_max(res)
    return [max(res), min(res)] if res else [0, 0]


# print(solution(["I 16", "D 1"]))  # 0 0
# print(solution(["I 7", "I 5", "I -5", "D -1"]))   # 7 5
# print(solution(["I 7", "I 7", "I 7", "D -1", "D -1", "D -1"]))  # 0 0
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))    # 333 -45
# print(solution(["I 2", "I 4", "D -1", "I 1", "D 1"]))   # 1 1
