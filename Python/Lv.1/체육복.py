def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)
    lost = sorted(list(lost_set - reserve_set))
    reserve = sorted(list(reserve_set - lost_set))
    
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
        elif i+1 in lost:
            lost.remove(i+1)
            
    return n - len(lost)

## 풀이전략, 핵심 아이디어
# 겹치는 학생(lost와 reserve에 모두 있는 학생)을 가장 먼저 제거
# 여벌이 있는 학생은 앞번호를 먼저 확인하고, 없으면 뒷번호 확인
