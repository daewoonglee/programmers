import pandas as pd


def solution(data, col, row_begin, row_end):
    df = pd.DataFrame(data, columns=[str(i) for i in range(len(data[0]))])
    df.sort_values(by=[str(col-1), "0"], ascending=[True, False], ignore_index=True, inplace=True)

    ans = 0
    for i in range(row_begin, row_end+1):
        # print(f"i: {i}, df[i]: {df.iloc[i]}, sum: {sum([v%(i+1) for v in df.iloc[i]])}")
        ans ^= sum([v % i for v in df.iloc[i-1]])
    return ans

"""
1. 입력된 data에서 col 열에 해당 값 기준으로 오름차순 정렬
    1-1. 동일한 값이 존재하면 1번째 값(기본키)을 기준으로 내림차순 정렬
2. row_begin <= i <= row_end 구간에서 해당 행 값 기준으로 mod 계산
3. 각 행마다 계산된 mod 값을 합침
4. 합쳐진 값들에 대해 xor 연산 계산
"""


print(solution([[2,2,6],[1,5,10],[4,2,9],[3,8,3]], 2, 2, 3)) # 4
