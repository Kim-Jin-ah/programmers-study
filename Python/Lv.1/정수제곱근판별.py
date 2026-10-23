def solution(n):
    answer = 0
    
    for i in range(1,n+1):
        if pow(i,2) == n:
            answer = pow((i+1),2)
            break
        else:
            answer = -1
    return answer

## 풀이전략, 핵심 아이디어
# 조건문을 사용, pow 공식 활용

# pow 사용하지 않을시
def solution(n):
    root = int(n ** 0.5)
    if root * root == n:
        return (root + 1) ** 2
    return -1
#  root = int(n ** 0.5) 은 기억하기!
