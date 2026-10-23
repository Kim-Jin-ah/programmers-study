def solution(n, left, right):
    answer = []
    
    for i in range(left,right+1):
        row = i // n
        col = i % n
        
        answer.append(max(row,col)+1)
        
    return answer

## 풀이전략, 핵심 아이디어
# 발상의 전환 필요!!
# 이차원 배열이라고 문제에서 주어져도 최대한 간단하고 빠르게 답을 구할 수 있는 방법을 사용하기
