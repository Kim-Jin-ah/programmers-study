def solution(A,B):
    answer = 0
    A.sort(reverse=True)
    B.sort()
    
    for i in range(len(A)):
        answer += A[i]*B[i]
    return answer

## 풀이전략, 핵심 아이디어
# 정렬을 활용하여 최소곱을 반복문을 통해 계산하고 더하기
