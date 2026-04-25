def solution(n):
    answer = 0
    while n > 0:
        answer += n % 10
        n //= 10
    return answer

## 풀이전략, 핵심 아이디어
# 자릿수라는 게 몇 번 반복을 돌려야 할 지 모르기 때문에 while을 사용하는 게 효율적일 거라 생각함
# 일의 자리부터 구하고, 그 순서대로 더하는 방식
  
# for문으로 해보기
# def solution(n):
#    answer = 0
#    for i in str(n):
#        answer += int(i)
#    return answer
