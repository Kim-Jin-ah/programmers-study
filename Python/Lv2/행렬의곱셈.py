def solution(arr1, arr2):
    answer = [[0] * len(arr2[0]) for _ in range(len(arr1))]
    
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr2)):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    
    return answer

## 풀이전략, 핵심아이디어
# 문제 이해가 어려웠음..
# 원리 파악이 우선 코드 짜기 전에 구조 먼저 생각하기
