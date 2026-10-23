def solution(arr):
    
    if len(arr) == 1:
        return [-1]
    
    arr.remove(min(arr))
    
    return arr

## 풀이전략, 핵심 아이디어
# 조건문만 잘 작성하면 어려울 건 없는 문제
# arr.remove() 공식과 그 안에 min(arr)이 들어갈 수 있다는 점만 주의
