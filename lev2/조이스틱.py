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
    asciis = [ord('A'), ord('N'), ord('Z')]

    n_list = [ord(n) - asciis[0] if ord(n) < asciis[1] else asciis[2] - ord(n) + 1 for i, n in enumerate(name)]
    idx = max([i for i, n in enumerate(n_list) if n], default=0)
    r_n_list = [n_list[0]] + n_list[1:][::-1]
    r_idx = max([i for i, n in enumerate(r_n_list) if n], default=0)

    return sum(n_list) + idx if idx < r_idx else sum(r_n_list) + r_idx


print(solution('JAZ'))      # 11
print(solution('JAZZAA'))   # 14
print(solution('JEROEN'))   # 56
print(solution('JAN'))      # 23
print(solution('ABA'))      # 2
print(solution('JANA'))     # 24
print(solution('AAA'))      # 0


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
