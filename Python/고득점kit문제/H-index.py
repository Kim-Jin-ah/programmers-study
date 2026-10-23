def solution(citations):
    citations.sort(reverse=True)
    
    for i in range(len(citations)):
        if citations[i] < i + 1:
            return i
    return len(citations)

## 풀이전략, 핵심 아이디어
# 정렬 + 인덱스 비교 만으로 풀 수 있는 문제
# 현재까지 i+1 편의 논문이 각각 i+1회 이상 인용되었는지 이해했는지가 핵심
