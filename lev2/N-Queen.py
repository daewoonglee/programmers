def solution(n):
    pass


print(solution(4)) # 2


"""
(포인트) 선택된 범위 제거한 리스트를 어떻게 만들 수 있는가?

    for d in range(n): 
        mat[i][d]=1 # 가로
        mat[d][j]=1 # 세로        
    왼위: for d in range(1,j): mat[i-d][j-d]=1
    왼아: for d in range(1,n-i): mat[i+d][j+d]=1
    오위: for d in range(1,n-j): mat[i-d][j+d]=1
    오아: for d in range(1,n-j): mat[i+d][j+d]=1

    사선 처리에 대한 일반화 수식을 못만들고있음, 현재 접근 방법으론 모든 경우의 수 처리 불가
"""
