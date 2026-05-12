def solution(s):
    answer = []
    s_split = s.split(" ")
    
    for sp in s_split:
        if sp == "Z":
            answer.pop()
        else:
            answer.append(int(sp))
            
    return sum(answer)

## 풀이전략, 핵심 아이디어
# stack 구조를 사용하여 pop과 append로 정리하고
# 마지막에 한번에 sum 해서 합계 구하기
