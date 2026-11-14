def solution(A, B):
    A.sort()
    B.sort()
    
    answer = 0
    i = 0
    j = 0
    
    while i < len(A) and j < len(B):
        if B[j] > A[i]:
            answer += 1
            i += 1
            j += 1
        else:
            j += 1

    return answer

## 풀이전략, 핵심 아이디어
# B팀의 숫자가 A팀보다 작거나 같다면 그 숫자는 버려도 된다 가 포인트
# else: 부분이 중요함
