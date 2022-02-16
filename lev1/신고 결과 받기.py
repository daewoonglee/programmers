def solution(id_list, report, k):
    report = list(set(report))
    ans = [0 for _ in range(len(id_list))]
    idx = {name: i for i, name in enumerate(id_list)}
    lookup = {name: [[], 0] for name in id_list}
    for r in report:
        n, r = r.split()
        lookup[r][-1] += 1
        lookup[r][0].append(n)
    
    for v in lookup.values():
        if v[-1] >= k:
            for name in v[0]:
                ans[idx[name]] += 1
    return ans


print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 1))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 1))

