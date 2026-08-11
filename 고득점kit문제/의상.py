def solution(clothes):
    dic = {}
    for i,j in clothes:
        dic[j] = dic.get(j,0) + 1
    
    answer = 1
    for value in dic.values():
        answer *= (value+1)
        
    return answer - 1

## 풀이전략, 핵심 아이디어
# dic.get()의 용도 정확히 파악
# 마지막에 +1 한 값을 곱해야한다 생각 필요!
