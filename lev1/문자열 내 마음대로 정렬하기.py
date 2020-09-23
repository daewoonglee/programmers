"""
문제 설명
문자열로 구성된 리스트 strings와, 정수 n이 주어졌을 때,
각 문자열의 인덱스 n번째 글자를 기준으로 오름차순 정렬하려 합니다.
예를 들어 strings가 [sun, bed, car]이고 n이 1이면 각 단어의 인덱스 1의 문자 u, e, a로 strings를 정렬합니다.

제한 조건
strings는 길이 1 이상, 50이하인 배열입니다.
strings의 원소는 소문자 알파벳으로 이루어져 있습니다.
strings의 원소는 길이 1 이상, 100이하인 문자열입니다.
모든 strings의 원소의 길이는 n보다 큽니다.
인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치합니다.

입출력 예
strings	n	return
[sun, bed, car]	1	[car, bed, sun]
[abce, abcd, cdx]	2	[abcd, abce, cdx]

입출력 예 설명
입출력 예 1
sun, bed, car의 1번째 인덱스 값은 각각 u, e, a 입니다.
이를 기준으로 strings를 정렬하면 [car, bed, sun] 입니다.

입출력 예 2
abce와 abcd, cdx의 2번째 인덱스 값은 c, c, x입니다.
따라서 정렬 후에는 cdx가 가장 뒤에 위치합니다.
abce와 abcd는 사전순으로 정렬하면 abcd가 우선하므로, 답은 [abcd, abce, cdx] 입니다.
"""


def solution(strings, n):
    # run time error in programmers site
    # 0.030307105499999997
    # sorted_strings = sorted(strings, key=lambda x: x[n], reverse=False)
    # duplication = [i for i in range(len(sorted_strings)-1) if sorted_strings[i][n] == sorted_strings[i+1][n]]
    # if duplication:
    #     sorted_duplication = sorted(sorted_strings[duplication[0]: duplication[0]+len(duplication)+1])
    #     for i in range(len(sorted_duplication)-1):
    #         sorted_strings[duplication[i]] = sorted_duplication[i]
    #     sorted_strings[duplication[-1]+1] = sorted_duplication[duplication[-1]+1]
    # return sorted_strings

    # 정렬하면서 중복되는 n자리수 인덱스 판단하면서 소팅
    # 중복되는 n자리수에 대하여 재소

    pass


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr


def quick_sort(n):
    if len(n) <= 2:
        print(f'return n: {n}')
        return n
    print(f'quick_sort: {n}')
    pivot = 0
    left = 1
    right = len(n) - 1
    while True:
        while n[left] < n[pivot] and left <= len(n):
            left += 1
        while n[right] > n[pivot] and right >= 0:
            right -= 1
        if left <= right:
            n = swap(n, left, right)
            print(f'swap n: {n}, l: {n[left]}, r: {n[right]}')
        else:
            if n[pivot] >= n[right]:
                n = swap(n, pivot, right)
            print(f'i==j n: {n}, l: {left}, r: {right}')
            quick_sort(n[:right])
            quick_sort(n[left:])


# print(quick_sort([5, 3, 8, 4, 9, 1, 6, 2, 7]))
print(quick_sort([5, 3, 7, 6, 2, 1, 4]))

# print(solution(['sun', 'bed', 'car'], 1))
# print(solution(['abce', 'abcd', 'cdx'], 2))
# print(solution(['abce', 'abcd', 'abcc'], 2))
# print(solution(['xzc', 'abce', 'abcd', 'abcc'], 2))

# import timeit
# avg_time = 0.
# tests = [[['sun', 'bed', 'car'], 1], [['abce', 'abcd', 'cdx'], 2], [['abce', 'abcd', 'abcc'], 2], [['xzc', 'abce', 'abcd', 'abcc'], 2]]
# for t in tests:
#     avg_time += timeit.timeit(lambda: solution(*t), number=10000)
# print(f'avg_time: {avg_time / len(tests)}')
