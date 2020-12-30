"""
문제 설명
조이스틱으로 알파벳 이름을 완성하세요. 맨 처음엔 A로만 이루어져 있습니다.
ex) 완성해야 하는 이름이 세 글자면 AAA, 네 글자면 AAAA

조이스틱을 각 방향으로 움직이면 아래와 같습니다.

▲ - 다음 알파벳
▼ - 이전 알파벳 (A에서 아래쪽으로 이동하면 Z로)
◀ - 커서를 왼쪽으로 이동 (첫 번째 위치에서 왼쪽으로 이동하면 마지막 문자에 커서)
▶ - 커서를 오른쪽으로 이동
예를 들어 아래의 방법으로 JAZ를 만들 수 있습니다.

- 첫 번째 위치에서 조이스틱을 위로 9번 조작하여 J를 완성합니다.
- 조이스틱을 왼쪽으로 1번 조작하여 커서를 마지막 문자 위치로 이동시킵니다.
- 마지막 위치에서 조이스틱을 아래로 1번 조작하여 Z를 완성합니다.
따라서 11번 이동시켜 "JAZ"를 만들 수 있고, 이때가 최소 이동입니다.
만들고자 하는 이름 name이 매개변수로 주어질 때, 이름에 대해 조이스틱 조작 횟수의 최솟값을 return 하도록 solution 함수를 만드세요.

제한 사항
name은 알파벳 대문자로만 이루어져 있습니다.
name의 길이는 1 이상 20 이하입니다.

입출력 예
name	return
JEROEN	56
JAN	    23

출처
※ 공지 - 2019년 2월 28일 테스트케이스가 추가되었습니다.
"""


def solution(name):
    # n_list = [min(ord(n) - ord('A'), ord('Z') - ord(n) + 1) for n in name]
    #
    # answer = 0
    # idx = 0
    # while 1:
    #     answer += n_list[idx]
    #     n_list[idx] = 0
    #     if not sum(n_list):
    #         break
    #
    #     # 0.035142608285714284
    #     # left = idx - 1
    #     # right = 1 + idx
    #     # l_step = 1
    #     # r_step = 1
    #     # while n_list[left] == 0:
    #     #     left -= 1
    #     #     l_step += 1
    #     # while n_list[right] == 0:
    #     #     right += 1
    #     #     r_step += 1
    #     # idx, step = [right, r_step] if r_step <= l_step else [left, l_step]
    #     # answer += step
    #
    #     # code refactoring 2 (reference for code refactoring1)
    #     left = 1
    #     right = 1
    #     while n_list[idx - left] == 0:
    #         left += 1
    #     while n_list[idx + right] == 0:
    #         right += 1
    #
    #     # code refactoring 2-1
    #     # 0.03441166342857143
    #     # idx, n = [idx + right, right] if right <= left else [idx - left, left]
    #     # answer += n
    #
    #     # code refactoring 2-2
    #     # 0.03316130271428572
    #     idx += -left if left < right else right
    #     answer += left if left < right else right
    #
    # return answer

    # code refactoring 1
    # 0.03448436142857143
    m = [min(ord(c) - ord('A'), ord('Z') - ord(c) + 1) for c in name]

    answer = 0
    where = 0
    while True:
        answer += m[where]
        m[where] = 0

        if sum(m) == 0:
            break

        left, right = (1, 1)

        while m[where - left] <= 0:
            left += 1
        while m[where + right] <= 0:
            right += 1

        answer += left if left < right else right
        where += -left if left < right else right

    return answer


# print(solution('JAZ'))         # 11
print(solution('JAZZAA'))      # 14
print(solution('JEROEN'))      # 56
print(solution('JAN'))         # 23
print(solution('ABA'))         # 2
print(solution('JANA'))        # 24
print(solution('AAA'))         # 0
print(solution('BBBAAAB'))     # 9
print(solution('ABABAAAAABA')) # 11
print(solution("BABAAAAB"))    # 7


import timeit
avg_time = 0.
tests = ['JAZ',
         'JAZZAA',
         'JEROEN',
         'JAN',
         'ABA',
         'JANA',
         'AAA']
for t in tests:
    avg_time += timeit.timeit(lambda: solution(t), number=10000)
print(f'avg_time: {avg_time / len(tests)}')
