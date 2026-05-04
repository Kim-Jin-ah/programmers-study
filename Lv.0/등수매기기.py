def solution(score):
    answer = []
    sums = [s[1] + s[0] for s in score]
    
    sorted_sums = sorted(sums, reverse=True)
    
    answer = [sorted_sums.index(s) + 1 for s in sums]
        
    return answer

## 풀이전략, 핵심아이디어
# 리스트 컴프리헨션 방식 사용으로 간결하게
# 내림차순 정렬한뒤, 인덱스로 순위 표현
