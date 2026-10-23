def solution(my_string):
    answer = ''
    answer = my_string[::-1]
    return answer

# 풀이전략, 핵심 아이디어
# 문자열, 리스트 뒤집는건 거의 [::-1] 원리 이용

# 이걸 반복문으로 접근한다면
def solution(my_string):
    answer = ''
    
    for s in my_string:
        answer = s + answer
        
    return answer

# 외우자!!
