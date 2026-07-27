def solution(mats, park):
    answer = 0
    mats.sort(reverse=True)
    row = len(park)
    col = len(park[0])
    
    for mat in mats:
        for i in range(row-mat+1):
            for j in range(col-mat+1):
                possible = True
                
                for x in range(i,i+mat):
                    for y in range(j,j+mat):
                        if park[x][y] != "-1":
                            possible = False
                if possible:
                    return mat
            
    return -1

## 풀이전략, 핵심 아이디어
# 모든 시작 위치를 탐색하고, 특정 크기의 부분 영역 검사
# 크기(mat):어떤 돗자리를 검사할지 / 시작위치(i,j):어디에 놓을지 / 내부위치(x,y):그 돗자리 영역이 모두 비어있는지 확인
