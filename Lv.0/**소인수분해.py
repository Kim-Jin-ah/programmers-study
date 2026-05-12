def solution(n):
    answer = []
    i = 2
    
    while n > 1:
        if n % i == 0:
            if i not in answer:
                answer.append(i)
            n //= i
        else:
            i += 1
            
    return answer

## 풀이전략, 핵심 아이디어
# 소인수분해의 최소인 2부터 나누기 시작
# 1부터 해당되지 않으므로 while n>1
# 나누어지면 정답에 추가하고, 아니라면 i에 1을 더하여 반복
