def solution(k, d):
    answer = 0
    dd = d*d
    for a in range(0,d+1,k):
        if a == 0:
            answer += (d//k)+1
            continue
        num = int((dd - a*a)**0.5)
        answer += (int(num) // k)+1
        
    return answer

## 풀이전략, 핵심 아이디어
# 피타고라스 정리 이용 및 점의 좌표가 항상 k의 배수여야 한다는 점 주의
# 숫자의 범위가 크므로 이중 for문 사용 x
