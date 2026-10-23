def solution(msg):
    dic = {}
    for i in range(26):
        dic[chr(65+i)] = i+1
    
    answer = []
    w = ""
    for c in msg:
        if w+c in dic:
            w = w+c
        else:
            answer.append(dic[w])
            dic[w+c] = len(dic)+1
            w = c
    if w:
        answer.append(dic[w])
        
    return answer

## 풀이전략, 핵심 아이디어
# 너무 어렵고, 복잡하게 생각하지 말기
# 문자열 더하기와 예외처리 부분 조심하기
# len(dic)+1 같은 것들 활용 잘하기
