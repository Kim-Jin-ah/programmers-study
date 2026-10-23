def solution(n):
    arr = [0,1]
    answer = 0
    
    for i in range(2,n+1):
        answer = arr[0]+arr[1]
        arr[0] = arr[1]
        arr[1] = answer
        
    return answer % 1234567

## 풀이전략, 핵심 아이디어
# 이전 값 2개만 필요하므로 변수 2개로 반복 갱신하기 가 핵심
# 다만, 위의 방식으로는 n=1의 처리 부분에서 안전하지 못함. 따라서
# def solution(n):
    a = 0
    b = 1
    
    for i in range(n):
        a, b = b, a + b
    
    return a % 1234567
# 또는
def solution(n):
    a = 0
    b = 1
    
    for i in range(n):
        a, b = b, (a + b) % 1234567
        
    return a
# 로 푸는 게 훨씬 간단함 참고
