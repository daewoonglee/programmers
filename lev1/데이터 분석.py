import pandas as pd


def solution(data, ext, val_ext, sort_by):
    # case 1
    # df = pd.DataFrame(data, columns=["code", "date", "maximum", "remain"])
    # return df[df[ext] <= val_ext].sort_values(by=sort_by).values.tolist()

    # case 2
    ext_dict = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    # return sorted([row for row in data if row[ext_dict[ext]] <= val_ext], key=lambda x: x[ext_dict[sort_by]])
    ans = [row for row in data if row[ext_dict[ext]] <= val_ext]
    ans.sort(key=lambda x: x[ext_dict[sort_by]])
    return ans




print(solution([[1, 20300104, 100, 80], [2, 20300804, 847, 37], [3, 20300401, 10, 8]], "date", 20300501, "remain")) # [[3,20300401,10,8],[1,20300104,100,80]])