def solution(age):
    answer = ''
    alpha = "abcdefghij"
    
    for i in str(age):
        answer += alpha[int(i)]
    return answer

## 풀이전략, 핵심 아이디어
# 각 자리 숫자를 문자열로 변환하는 것이 핵심
# 이후 aplha를 이용해 알파벳으로 치환
