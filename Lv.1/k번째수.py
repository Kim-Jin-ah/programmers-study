def solution(array, commands):
    answer = []
    
    for a,b,c in commands:
        answer.append(sorted(array[a-1:b])[c-1])
        
    return answer

## 풀이전략, 핵심 아이디어
# 슬라이싱 -> 정렬 -> k번째 값 추출 순서로 진행
# 슬라이싱과 언패킹 방식을 알면 쉽게 풀 수 있는 문제였음
