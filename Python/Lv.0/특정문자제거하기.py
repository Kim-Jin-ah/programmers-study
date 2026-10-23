def solution(my_string, letter):
    answer = ''
    for i in my_string:
        if i == letter:
            continue
        answer += i
    return answer

## 풀이전략, 핵심 아이디어
# 반복문의 continue 사용하면 해당 문자 없이 반복진행됨을 이용

# 근데 다른 쉬운 방법이 있었음..
#def solution(my_string, letter):
#    return my_string.replace(letter, '')
