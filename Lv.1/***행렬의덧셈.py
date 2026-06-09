def solution(arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        row = []
        
        for j in range(len(arr1[0])):
            row.append(arr1[i][j] + arr2[i][j])
            
        answer.append(row)
    
    return answer

## 풀이 전략, 핵심 아이디어
# 이중 반복문을 사용해 각 행과 열을 순회해야함
# arr1[i][j] + arr2[i][j]
# 행렬은 2차원 리스트
