def solution(n):
    for i in range(n):# q의 시작지점을 0~n-1 달리하면서 탐색
        for j in range(i, n):
            mat = [[0]*n for _ in range(n)]
            for z in range(n):
                if mat[j][z] == 0:
                    for x in range(n): mat[j][x] = 1 # 가로
                    for y in range(n): mat[y][z] = 1 # 세로


print(solution(4)) # 2


"""
0번째 인덱스 기준에서 0~n-1까지 돌면서 모든 경우 확인
    0번째 인덱스 0으로 선택한 경우
        1번째 인덱스에서 0번째 0인덱스에서 선택된 범위 제거한 리스트에서 선택할 수 있는 경우 선택
        * 1번째 인덱스의 2번째 선택한 경우
                      3번째 선택한 경우
                      n-1번째 선택한 경우에 대해서 다른 가지수 있을 수 있음 (여기에 대한 해결방안 필요)
        2번째 인덱스에서 0,1번째 인덱스에서 선택된 범위 제거한 리스트에서 선택할 수 있는 경우 선택
        n-1번째 인덱스까지 반복
        
        (포인트) 선택된 범위 제거한 리스트를 어떻게 만들 수 있는가?
        제거방법
            가로: for y in range(n): mat[i][y]=1
            세로: for x in range(n): mat[x][j]=1
            왼위: for y in range(j): mat[i-y][j-y]=1
            왼아: for y in range(n-i): mat[i+y][j+y]=1 왼쪽 부분에 대한 해당 [i][j]에 대한 중복처리 발생 (해결방안 필요)
            오위: for y in range(n-i): mat[i-y][j+y]=1 # 1개 더 돌듯 (해결방안 필요)
            오아: for y in range(n-i): mat[i+y][j+y]=1
        
            사선 처리할 때 공통점이 있어보임 여기에 대한 처리 필요
"""
