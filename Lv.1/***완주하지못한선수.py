def solution(participant, completion):
    dic = {}
    
    for i in participant:
        dic[i] = dic.get(i,0) + 1
        
    for j in completion:
        dic[j] -= 1
        
    for key in dic:
        if dic[key] > 0:
            return key

## 풀이전략, 핵심 아이디어
# dic[i] = dic.get(i,0) + 1 가 핵심(딕셔너리 사용, 중복 데이터 숫자로 처리)
# 단순 구현보다 적합한 자료구조를 선택하여 풀이하는 것에 집중하기
