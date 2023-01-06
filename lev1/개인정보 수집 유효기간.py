from datetime import datetime


def solution(today, terms, privacies):
    tdy = datetime(*map(int, today.split(".")))
    term_dict = {t[0]: int(t[2:]) for t in terms} # {t.split()[0]: t.split()[1] for t in terms}

    ans = []
    for i, p in enumerate(privacies):
        d, t = p.split()
        dy, dm, dd = map(int, d.split("."))

        dm += term_dict[t] - 1
        dy += dm // 12
        dm = dm % 12 + 1
        date = datetime(dy, dm, dd)

        if tdy >= date:
            ans.append(i+1)
    return ans


print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"])) # [1, 3]
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"])) # [1, 4, 5]
print(solution("2022.10.01", ["Z 100"], ["2000.01.01 Z", "2013.01.01 Z", "2014.05.28 Z", "2014.06.01 Z", "2014.06.02 Z"]))

