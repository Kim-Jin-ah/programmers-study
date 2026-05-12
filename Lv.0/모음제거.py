def solution(my_string):
    answer = ''
    for str in my_string:
        if str not in "aeiou":
            answer += str
    return answer

## 풀이 전략, 핵심 아이디어
# "aeiou" 로 한번에 물어볼 수 있음! 기억하기
