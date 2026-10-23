def solution(s, skip, index):
    answer = ''
    for i in s:
        count = 0
        while count < index:
            if i == 'z':
                i = 'a'
            else:
                i = chr(ord(i)+1)
            
            if i not in skip:
                count += 1
        answer += i
        
    return answer

## 풀이전략, 핵심 아이디어
# for 로 문자열의 각 문자를 꺼내고, while로 유효한 이동을 Index번까지 한다
# c가 z인 경우와 아닌경우를 나누어 조건문을 쓴다(아스키코드 활용)
