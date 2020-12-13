"""
문제 설명
초 단위로 기록된 주식가격이 담긴 배열 prices가 매개변수로 주어질 때, 가격이 떨어지지 않은 기간은 몇 초인지를 return 하도록 solution 함수를 완성하세요.

제한사항
prices의 각 가격은 1 이상 10,000 이하인 자연수입니다.
prices의 길이는 2 이상 100,000 이하입니다.

입출력 예
prices	        return
[1, 2, 3, 2, 3]	[4, 3, 1, 1, 0]

입출력 예 설명
1초 시점의 ₩1은 끝까지 가격이 떨어지지 않았습니다.
2초 시점의 ₩2은 끝까지 가격이 떨어지지 않았습니다.
3초 시점의 ₩3은 1초뒤에 가격이 떨어집니다. 따라서 1초간 가격이 떨어지지 않은 것으로 봅니다.
4초 시점의 ₩2은 1초간 가격이 떨어지지 않았습니다.
5초 시점의 ₩3은 0초간 가격이 떨어지지 않았습니다.
※ 공지 - 2019년 2월 28일 지문이 리뉴얼되었습니다.
"""


def solution(prices):
    # 0.02500254016666667
    # N = len(prices)
    # answer = [-1] * N
    # for i in range(N):
    #     for j in range(i+1, N):
    #         if prices[i] > prices[j]:
    #             answer[i] = j-i
    #             break
    #     if answer[i] == -1:
    #         answer[i] = N-i-1
    # return answer

    # code refactoring
    # 0.022989750333333333
    N = len(prices)
    ans = [0] * N
    stack = [0]
    for i in range(1, N):
        if prices[i] < prices[stack[-1]]:
            for j in stack[::-1]:
                if prices[i] < prices[j]:
                    ans[j] = i-j
                    stack.remove(j)
                else:
                    break
        stack.append(i)
    for i in range(0, len(stack)-1):
        ans[stack[i]] = N - stack[i] - 1
    return ans


# print(solution([1, 2, 3, 2, 3]))
# print(solution([1, 2, 3, 1, 3]))
# print(solution([5, 4, 3, 2, 1]))
print(solution([1, 2, 3, 4, 5]))
# print(solution([5, 5, 5, 5, 5]))


import timeit
avg_time = 0.
tests = [[1, 2, 3, 2, 3],
         [5, 4, 3, 2, 1],
         [5, 1],
         [5, 4, 10, 5],
         [5, 5, 5, 5],
         [1, 5, 6, 5, 2, 4, 77, 0]]
for t in tests:
    avg_time += timeit.timeit(lambda: solution(t), number=10000)
print(f'avg_time: {avg_time / len(tests)}')
