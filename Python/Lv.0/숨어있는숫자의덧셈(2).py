def solution(my_string):
    answer = 0
    num=''
    for char in my_string:
        if char.isdigit():
            num += char
        else:
            if num:
                answer += int(num)
                num=''
    if num:
        answer += int(num)
                
    return answer

## 풀이전략, 핵심 아이디어
# 문자 내에 숫자가 들어있는지 확인이 우선
# 그 다음 숫자가 들어있다면 answer에 넣고 계산. 초기화
# 반복
