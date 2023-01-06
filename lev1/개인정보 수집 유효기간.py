def solution(today, terms, privacies):
    ty, th, td = map(int, today.split("."))
    term_dict = {t[0]: int(t[2:]) for t in terms} # {t.split()[0]: t.split()[1] for t in terms}

    ans = []
    for i, p in enumerate(privacies):
        d, t = p.split()
        dy, dh, dd = map(int, d.split("."))

        q, d = divmod(dh + term_dict[t], 12)
        dy += q
        dh = d

        # print(f"t: {ty}, {th}, {td} | d: {dy}, {dh}. {dd}, flag: {dy < ty and dh < th and dd < td}")
        if dy < ty or dh <= th and dd <= td:
            ans.append(i+1)
    return ans


print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])) # [1, 3]
print(solution("2020.01.01", ["Z 3", "D 5"]	, ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])) # [1, 4, 5]
