def solution(t, p):
    answer = 0
    
    for i in range(len(t)-len(p)+1):
        slic = t[i:i+len(p)]
        if int(slic) <= int(p):
            answer += 1

    return answer

## 풀이전략, 핵심 아이디어
# 길이가 n인 문자열에서 길이가 m인 연속 부분문자열 개수는 n - m + 1 인것 기억하기!!
