def solution(edges):
    max_node = max(max(a,b) for a,b in edges)
    indegree = [0] * (max_node + 1)
    outdegree = [0] * (max_node + 1)
    
    for a,b in edges:
        outdegree[a] += 1
        indegree[b] += 1
    
    answer = [0,0,0,0]
    
    for i in range(1,max_node + 1):
        if indegree[i] == 0 and outdegree[i] >= 2:
            answer[0] = i
            break
    
    stick = 0
    eight = 0
    for i in range(1,max_node + 1):
        if i == answer[0]:
            continue
        
        if indegree[i] > 0 and outdegree[i] == 0:
            stick += 1
        elif indegree[i] >= 2 and outdegree[i] == 2:
            eight += 1
    
    total = outdegree[answer[0]]
    donut = total - stick - eight
    
    answer[1] = donut
    answer[2] = stick
    answer[3] = eight
    
    return answer

## 풀이전략, 핵심 아이디어
# 들어오는 화살표와 나가는 화살표의 개수를 세서 생성된 정점과 각 그래프 판단
