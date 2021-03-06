"""
문제 설명
무인도에 갇힌 사람들을 구명보트를 이용하여 구출하려고 합니다. 구명보트는 작아서 한 번에 최대 2명씩 밖에 탈 수 없고, 무게 제한도 있습니다.

예를 들어, 사람들의 몸무게가 [70kg, 50kg, 80kg, 50kg]이고 구명보트의 무게 제한이 100kg이라면
2번째 사람과 4번째 사람은 같이 탈 수 있지만 1번째 사람과 3번째 사람의 무게의 합은 150kg이므로
구명보트의 무게 제한을 초과하여 같이 탈 수 없습니다.

구명보트를 최대한 적게 사용하여 모든 사람을 구출하려고 합니다.

사람들의 몸무게를 담은 배열 people과 구명보트의 무게 제한 limit가 매개변수로 주어질 때,
모든 사람을 구출하기 위해 필요한 구명보트 개수의 최솟값을 return 하도록 solution 함수를 작성해주세요.

제한사항
무인도에 갇힌 사람은 1명 이상 50,000명 이하입니다.
각 사람의 몸무게는 40kg 이상 240kg 이하입니다.
구명보트의 무게 제한은 40kg 이상 240kg 이하입니다.
구명보트의 무게 제한은 항상 사람들의 몸무게 중 최댓값보다 크게 주어지므로 사람들을 구출할 수 없는 경우는 없습니다.

입출력 예
people	            limit	return
[70, 50, 80, 50]	100	    3
[70, 80, 50]	    100 	3
"""


def solution(people, limit):
    # 0.010046831000000003
    # people.sort()
    # i = 0
    # j = len(people)
    # while i < j:
    #     if people[j-1] + people[i] <= limit:
    #         i += 1
    #     j -= 1
    # return len(people)-j

    # code refactoring
    # 0.009212844000000001
    answer = 0
    people.sort()
    i = 0
    j = len(people) - 1
    while i < j:
        if people[j] + people[i] <= limit:
            i += 1
            answer += 1
        j -= 1
    return len(people) - answer


print(solution([70, 50, 80, 50], 100))              # 3
print(solution([70, 50, 80, 50, 50], 100))          # 4
print(solution([70, 80, 50], 100))                  # 3
print(solution([70, 80, 50, 90, 100], 100))         # 5
print(solution([40] * 13, 240))                     # 7
print(solution([60] * 8, 240))                      # 4
print(solution([60] * 9, 240))                      # 5
print(solution([1, 10, 1, 10, 20], 21))             # 3
print(solution([1, 2, 3, 4, 5], 5))                 # 3
print(solution([1, 2, 2, 2, 3, 3, 3, 4, 4, 4], 7))  # 5



import timeit
avg_time = 0.
tests = [[[70, 50, 80, 50], 100],
         [[70, 50, 80], 100],
         [[240, 240, 240], 240],
         [[40, 40, 40], 240],
         [[60, 60, 60, 60, 60], 240],
         [[1, 10, 1, 10, 20], 21],
         [[1, 2, 3, 4, 5], 5]]
for t in tests:
    avg_time += timeit.timeit(lambda: solution(*t), number=10000)
print(f'avg_time: {avg_time / len(tests)}')
