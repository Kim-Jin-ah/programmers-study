def solution(data, ext, val_ext, sort_by):
    answer = []
    dic = {"code":0,"date":1,"maximum":2,"remain":3}
    
    for i in data:
        if i[dic[ext]] < val_ext:
            answer.append(i)
    answer.sort(key=lambda x:x[dic[sort_by]])
    return answer

## 풀이전략, 핵심 아이디어
# 딕셔너리로 인덱스 활용하기
# 람다함수로 특정값 기준으로 정렬하기
