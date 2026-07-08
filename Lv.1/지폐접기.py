def solution(wallet, bill):
    answer = 0
    
    while (min(bill) > min(wallet)) or max(bill) > max(wallet):
        if bill[0] > bill[1]:
            bill[0] //= 2
        else:
            bill[1] //= 2
        answer += 1
        
    return answer

## 풀이전략, 핵심 아이디어
# 큰 변을 계속 반으로 접으면서, 명함 크기 안에 들어갈 때까지 반복
# 더 긴 변을 접는 것이 가장 효율적임을 먼저 생각하기
