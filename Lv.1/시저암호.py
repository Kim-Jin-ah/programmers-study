def solution(s, n):
    answer = ''
    
    for ch in s:
        if ch == ' ':
            answer += ' '
        elif ch.isupper():
            answer += chr((ord(ch)-ord('A')+n) % 26 + ord('A'))
        else:
            answer += chr((ord(ch)-ord('a')+n) % 26 + ord('a'))
            
    return answer

## 풀이전략, 핵심 아이디어
# 문자와 아스키코드 변환
  
# A,a를 기준으로 0~25로 변환 후 n만큼 이동시키고
# %26으로 순환시킨 후 다시 문자로 변환시킴
# 빈 공간일 경우도 조건문에 잊지말고 넣기

# 문자열을 한 글자씩 읽으면서 규칙에 따라 변환하는 형태를 구현해보는 연습 필요
