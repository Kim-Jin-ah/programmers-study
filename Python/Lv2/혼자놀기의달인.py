def solution(cards):
    visited = [False] * len(cards)
    groups = []
    for i in range(len(cards)):
        if visited[i]:
            continue
            
        count = 0
        current = i
        while not visited[current]:
            visited[current] = True
            count += 1
            current = cards[current] - 1
            
        groups.append(count)
        
    groups.sort(reverse=True)
    
    if len(groups) < 2:
        return 0
    
    return groups[0] * groups[1]

## 풀이전략, 핵심 아이디어
# visited로 상자를 중복 방문하지 않게 하기
# while문으로 하나의 그룹을 끝까지 탐색한 후
# 그룹 크기를 정렬해서 가장 큰 두 개 곱하기
