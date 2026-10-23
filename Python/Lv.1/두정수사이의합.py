def solution(a, b):
    answer = 0
    
    for i in range(min(a,b),max(a,b)+1):
        answer += i
        
    return answer

## 풀이전략, 핵심 아이디어
# 반복문의 범위를 min(a,b) , max(a,b)+1 로 설정가능하다는 것
# 더하기는 += 로 한번에 실행가능
# 또는
def solution(a,b):
  return sum(range(min(a,b), max(a,b)+1)
