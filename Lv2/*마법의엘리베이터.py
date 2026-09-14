def solution(storey):
    answer = 0
    
    while storey > 0:
        num = storey % 10
        
        if num < 5:
            answer += num
            storey //= 10
        elif num > 5:
            answer += 10 - num
            storey = storey // 10 + 1
        else:
            digit = (storey // 10) % 10
            
            if digit >= 5:
                answer += 5
                storey = storey // 10 + 1
            else:
                answer += 5
                storey //= 10
    return answer

## 풀이전략, 핵심 아이디어
# 단위를 10으로 잡고 몫과 나머지를 생각해서 조건문 작성.
# 아무리 많은 자릿수를 가진 숫자이더라도 이런식으로 해결해보기 
