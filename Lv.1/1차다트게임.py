def solution(dartResult):
    score = []
    i = 0
    while i < len(dartResult):
        if dartResult[i].isdigit():
            if dartResult[i] == '1' and i+1 < len(dartResult) and dartResult[i+1] == '0':
                num = 10
                i += 2
            else:
                num = int(dartResult[i])
                i += 1
            
            if dartResult[i] == 'S':
                num **= 1
            elif dartResult[i] == 'D':
                num **= 2
            elif dartResult[i] == 'T':
                num **= 3
            
            score.append(num)
            i += 1
            
            if i < len(dartResult):
                if dartResult[i] == '*':
                    score[-1] *= 2
                    if len(score) > 1:
                        score[-2] *= 2
                    i += 1
                elif dartResult[i] == '#':
                    score[-1] *= -1
                    i += 1
        
    return sum(score)

## 풀이전략, 핵심 아이디어
# 숫자 구분(1~10), 문자(S,D,T)가 왔을 때 숫자계산, 특수문자(*,#)이 왔을 때 계산...
# 풀이 구상을 전체적으로 틀을 잡은 뒤에 한줄씩 풀이 적어보는 연습하기. 무턱대고 적지말고!!
