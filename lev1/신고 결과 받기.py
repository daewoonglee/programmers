def solution(id_list, report, k):
    # 0.13976883329451084
    #ans = [0 for _ in range(len(id_list))]

    # code refactoring - 0.12620110251009464
    ans = [0] * len(id_list)
    idx = {name: i for i, name in enumerate(id_list)}
    #lookup = {name: [[], 0] for name in id_list}
    #for r in set(report):
    #    n, r = r.split()
    #    lookup[r][-1] += 1
    #    lookup[r][0].append(n)

    #for value in lookup.values():
    #    if value[-1] >= k:
    #        for v in value[0]:
    #            ans[idx[v]] += 1
    #return ans

    # code refactoring (R) - 0.11146278865635395
    lookup = {name: [] for name in id_list}
    for i in set(report):
        n, r = i.split()
        lookup[r].append(n)

    for values in lookup.values():
        if len(values) >= k:
            for v in values:
                ans[idx[v]] += 1
    return ans



print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 1))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 1))


if __name__ == "__main__":
    from timeit import Timer
    query = [[["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2], [["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 1], [["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3], [["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 1]]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10000))

