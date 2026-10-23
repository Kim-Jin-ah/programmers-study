def solution(array):
    
    array.sort()
    return array[len(array) // 2]

## 풀이전략, 핵심 아이디어
# 정렬 후 가운데 인덱스 찾기가 핵심
