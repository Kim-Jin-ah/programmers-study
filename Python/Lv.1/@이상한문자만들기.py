def solution(s):
    answer = ''
    idx = 0
    
    for ch in s:
        if ch == " ":
            answer += " "
            idx = 0
        else:
            if idx % 2 == 0:
                answer += ch.upper()
            else:
                answer += ch.lower()
            idx += 1
            
    return answer

## 풀이전략, 핵심 아이디어
# 문자 하나씩 순회하면서 공백을 만나면 인덱스를 0으로 초기화하는 방식 사용
# 처음 접근이 중요함. 인덱스 활용하는 문제 더 풀어봐야함
