"""
문제 설명
H-Index는 과학자의 생산성과 영향력을 나타내는 지표입니다. 어느 과학자의 H-Index를 나타내는 값인 h를 구하려고 합니다.
위키백과1에 따르면, H-Index는 다음과 같이 구합니다.

어떤 과학자가 발표한 논문 n편 중, h번 이상 인용된 논문이 h편 이상이고 나머지 논문이 h번 이하 인용되었다면 h의 최댓값이 이 과학자의 H-Index입니다.

어떤 과학자가 발표한 논문의 인용 횟수를 담은 배열 citations가 매개변수로 주어질 때,
이 과학자의 H-Index를 return 하도록 solution 함수를 작성해주세요.

제한사항
과학자가 발표한 논문의 수는 1편 이상 1,000편 이하입니다.
논문별 인용 횟수는 0회 이상 10,000회 이하입니다.

입출력 예
citations	        return
[3, 0, 6, 1, 5]	    3

입출력 예 설명
이 과학자가 발표한 논문의 수는 5편이고, 그중 3편의 논문은 3회 이상 인용되었습니다.
그리고 나머지 2편의 논문은 3회 이하 인용되었기 때문에 이 과학자의 H-Index는 3입니다.

※ 공지 - 2019년 2월 28일 테스트 케이스가 추가되었습니다.
"""


def solution(citations):
    # 0.04678369051543996
    # answer = 0
    # for h in range(1, len(citations)+1):
    #     up_c = len([1 for c in citations if c >= h])
    #     down_c = len([0 for c in citations if c <= h])
    #     if down_c <= h <= up_c:
    #         answer = h
    # return answer

    # code refactoring
    # 0.009623674326576293
    citations.sort()
    n = len(citations)
    for i in range(n):
        if citations[i] >= n - i:
            return n - i
    return 0

    # 0.02530302049126476
    # citations.sort(reverse=True)
    # return max(map(min, enumerate(citations, start=1)))


# print(solution([3, 0, 6, 1, 5]))
# print(solution([3, 0, 6, 1, 5, 4]))
# print(solution([5]))
# print(solution([5, 4, 10, 5]))
# print(solution([5, 5, 5, 5]))
print(solution([1, 5, 6, 5, 2, 4, 77, 0]))

# import timeit
# avg_time = 0.
# tests = [[3, 0, 6, 1, 5],
#          [3, 0, 6, 1, 5, 4],
#          [5],
#          [5, 4, 10, 5],
#          [5, 5, 5, 5],
#          [1, 5, 6, 5, 2, 4, 77, 0]]
# for t in tests:
#     avg_time += timeit.timeit(lambda: solution(t), number=10000)
# print(f'avg_time: {avg_time / len(t)}')
