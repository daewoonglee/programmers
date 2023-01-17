import pandas as pd
from functools import reduce


def solution(data, col, row_begin, row_end):
    # # 1.038903825
    # df = pd.DataFrame(data, columns=[str(i) for i in range(len(data[0]))])
    # df.sort_values(by=[str(col-1), "0"], ascending=[True, False], ignore_index=True, inplace=True)
    #
    # ans = 0
    # for i in range(row_begin, row_end+1):
    #     # print(f"i: {i}, df[i]: {df.iloc[i]}, sum: {sum([v%(i+1) for v in df.iloc[i]])}")
    #     ans ^= sum([v % i for v in df.iloc[i-1]])
    # return ans

    # code refactoring - # 0.013904737
    data.sort(key=lambda x: (x[col-1], -x[0]))
    return reduce(lambda x, y : x ^ y,
                  [sum([v % i for v in data[i - 1]]) for i in range(row_begin, row_end + 1)])


print(solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]], 2, 2, 3)) # 4


if __name__ == "__main__":
    from timeit import Timer
    query = [
        [[[2,2,6],[1,5,10],[4,2,9],[3,8,3]], 2, 2, 3],
        [[[1,2,3] for _ in range(1000)], 2, 400, 900],
        [[[1,2,3] for _ in range(1000)], 2, 1, 900]
    ]
    t = Timer(f"for t in {query}: solution(*t)", "from __main__ import solution")
    print(t.timeit(number=10))
