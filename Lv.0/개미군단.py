def solution(hp):
    answer = 0
    
    answer += (hp//5)
    hp %= 5
    
    answer += (hp // 3)
    hp %= 3
    
    answer += hp
    
    return answer

## 풀이전략, 핵심 아이디어
# 너무 어렵게 생각하지 말기
# += 뒤에 또 연산와도 돼
# 마지막엔 +1이니까 += hp로 해도 된다는 것 기억
