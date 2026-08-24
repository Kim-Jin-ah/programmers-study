def solution(s):
    answer = ''
    numbers = list(map(int,s.split()))
    
    return str(min(numbers)) + " " + str(max(numbers))

## 풀이전략, 핵심 아이디어
# map 사용과 str 붙이는 방식 활용방법 익히기
