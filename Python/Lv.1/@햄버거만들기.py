def solution(ingredient):
    answer = 0
    burger = []
    
    for i in ingredient:
        burger.append(i)
        
        if burger[-4:] == [1,2,3,1]:
            answer += 1
            
            burger.pop()
            burger.pop()
            burger.pop()
            burger.pop()
    
    return answer

## 풀이전략, 핵심 아이디어
# 스택을 리스트로 구현하는 문제
# 유형 익히기 & 다시 풀어보기
