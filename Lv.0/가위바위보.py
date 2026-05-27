def solution(rsp):
    answer = ''
    
    for i in rsp:
        if i == "2":
            answer += "0"
        elif i == "0":
            answer += "5"
        elif i == "5":
            answer += "2"
    return answer

## 풀이 전략, 핵심 아이디어
# 연속으로 나오는 경우도 있으므로 반복문 사용! -> 주의!!
# 나머지는 if문으로 쉽게 해결 가능
