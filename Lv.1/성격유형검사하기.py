def solution(survey, choices):
    answer = ''
    dic = {1:3, 2:2, 3:1, 5:1, 6:2, 7:3}
    result = {"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    
    for i in range(len(survey)):
        score = dic.get(choices[i])
        if choices[i] < 4:
            result[survey[i][0]] += score
        elif choices[i] > 4:
            result[survey[i][1]] += score
    
    if result["R"] >= result["T"]:
        answer += "R"
    else:
        answer += "T"
        
    if result["C"] >= result["F"]:
        answer += "C"
    else:
        answer += "F"
        
    if result["J"] >= result["M"]:
        answer += "J"
    else:
        answer += "M"
        
    if result["A"] >= result["N"]:
        answer += "A"
    else:
        answer += "N"
    
    return answer

## 풀이전략, 핵심 아이디어
# 문법 활용을 적극적으로 하여 계산 효율 줄이자!!
score = {
        "R":0, "T":0,
        "C":0, "F":0,
        "J":0, "M":0,
        "A":0, "N":0
    }

    for s, c in zip(survey, choices):
        if c < 4:
            score[s[0]] += 4 - c
        elif c > 4:
            score[s[1]] += c - 4
# 이렇게 하면 훨씬 간단하고 쉽게 풀 수 있어... 인덱스 굳이 안써도 되는 방법이 존재하니까,, 어렵게 가지말자,,,
