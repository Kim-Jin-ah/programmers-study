def solution(triangle):
    for i in range(1,len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:
                triangle[i][j] += triangle[i-1][j]
            elif j == len(triangle[i]) - 1:
                triangle[i][j] += triangle[i-1][j-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1],triangle[i-1][j])
                
    return max(triangle[-1])

## 풀이전략, 핵심 아이디어
# 현재 위치까지의 최대 합을 저장하는 것이 핵심
# 가장 왼쪽과 오른쪽은 접근할 수 있는 이전 위치가 하나임을 고려하여 누적합 구하기
