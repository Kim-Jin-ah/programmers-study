def solution(emergency):
    answer = []
    sorted_list = sorted(emergency,reverse=True)
    
    for i in emergency:
        answer.append(sorted_list.index(i)+1)
    
    return answer

## 풀이전략, 핵심 아이디어
# 내림차순 정렬한 후 그 순서로의 인덱스를 활용한다
# 내림차순하지 않은 것에 반복문을 돌리고, 내림차순한 인덱스를 넣으면 정답과 맞게 들어가진다
# 원래 위치 기준 결과를 반환해야한다는 점이 핵심
# 따라서 정렬 후 그 순위를 각각 넣은것
