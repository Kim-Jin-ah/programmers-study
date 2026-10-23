def solution(players, callings):
    dic = {}
    
    for idx, p in enumerate(players):
        dic[p] = idx
    
    for call in callings:
        idx = dic[call]
        front = players[idx-1]
        players[idx-1],players[idx] = players[idx],players[idx-1]
        
        dic[call] = idx -1
        dic[front] = idx
    return players

## 풀이전략, 핵심 아이디어
# 리스트의 순서바꾸기를 아는 것이 핵심! + 딕셔너리의 특성 활용
# 다시 풀어보자,,,
