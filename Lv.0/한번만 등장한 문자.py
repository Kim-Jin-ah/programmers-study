def solution(s):
    answer = ''
    for i in s:
        if s.count(i)== 1:
            answer+=i
    return ''.join(sorted(answer))

    return answer

## 풀이전략, 핵심아이디어
# 문자열을 결과에 합칠 땐 ''.join() 기억하기!!
