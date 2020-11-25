"""
문제 설명
Leo는 카펫을 사러 갔다가 아래 그림과 같이 중앙에는 노란색으로 칠해져 있고 테두리 1줄은 갈색으로 칠해져 있는 격자 모양 카펫을 봤습니다.

carpet.png

Leo는 집으로 돌아와서 아까 본 카펫의 노란색과 갈색으로 색칠된 격자의 개수는 기억했지만, 전체 카펫의 크기는 기억하지 못했습니다.

Leo가 본 카펫에서 갈색 격자의 수 brown, 노란색 격자의 수 yellow가 매개변수로 주어질 때 카펫의 가로, 세로 크기를 순서대로 배열에 담아 return 하도록 solution 함수를 작성해주세요.

제한사항
갈색 격자의 수 brown은 8 이상 5,000 이하인 자연수입니다.
노란색 격자의 수 yellow는 1 이상 2,000,000 이하인 자연수입니다.
카펫의 가로 길이는 세로 길이와 같거나, 세로 길이보다 깁니다.

입출력 예
brown	yellow	return
10	    2	    [4, 3]
8	    1	    [3, 3]
24	    24	    [8, 6]

출처
※ 공지 - 2020년 2월 3일 테스트케이스가 추가되었습니다.
※ 공지 - 2020년 5월 11일 웹접근성을 고려하여 빨간색을 노란색으로 수정하였습니다.
"""


def solution(brown, yellow):
    # 0.020155151
    # divisor = [i for i in range(1, yellow+1) if yellow % i == 0]
    # pivot = len(divisor)//2
    # if len(divisor) % 2:
    #     h = divisor[pivot] + 2
    #     if h*h == brown + yellow:
    #         return [h, h]
    #     divisor.pop(pivot)
    # for i in range(pivot):
    #     h = divisor[pivot-i-1] + 2
    #     w = divisor[pivot+i] + 2
    #     if h*w == brown + yellow:
    #         return [w, h]

    # code refactoring
    # 0.011519009714285714
    # for i in range(1, int(yellow**(1/2))+1):
    #     if yellow % i == 0:
    #         if 2*(i + yellow//i) == brown-4:
    #             return [yellow//i+2, i+2]

    # 0.014715602857142854
    # nm = brown + yellow
    # for n in range(1, nm+1):
    #     if nm % n != 0:
    #         continue
    #     m = nm//n
    #     if (n-2)*(m-2) == yellow:
    #         return sorted([n, m], reverse = True)

    # 0.012528091142857144
    import math
    # w = ((brown+4)/2 + math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    # h = ((brown+4)/2 - math.sqrt(((brown+4)/2)**2-4*(brown+yellow)))/2
    # return [w,h]

    ans=((brown-4)+math.sqrt((brown-4)**2-16*yellow))//4
    return [ans+2,yellow//ans+2]


print(solution(8, 1))   # 3, 3
print(solution(10, 2))  # 4, 3
print(solution(24, 24)) # 8, 6
print(solution(26, 10)) # 12, 3
print(solution(22, 14)) # 9, 4
print(solution(20, 16)) # 6, 6
print(solution(38, 16)) # 18, 3



import timeit
avg_time = 0.
tests = [[8, 1],
         [10, 2],
         [24, 24],
         [26, 10],
         [22, 14],
         [20, 16],
         [38, 16]]
for t in tests:
    avg_time += timeit.timeit(lambda: solution(*t), number=10000)
print(f'avg_time: {avg_time / len(tests)}')
