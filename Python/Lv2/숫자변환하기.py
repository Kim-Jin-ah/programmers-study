from collections import deque
def solution(x, y, n):
    queue = deque([(x,0)])
    visited = set([x])
    
    while queue:
        current,count = queue.popleft()
        if current == y:
            return count
        
        for num in [current+n,current*2,current*3]:
            if num <= y and num not in visited:
                queue.append((num,count+1))
                visited.add(num)
    return -1

## 풀이전략, 핵심 아이디어
# 현재 숫자에서 3가지 선택지가 계속 생기는 문제
# 따라서, BFS로 현재 숫자와 몇 번 연산했는지 같이 저장하면서 탐색. 이미 방문한 숫자는 set()을 이용해 다시 탐색하지 않도록.

# 현재 숫자 하나에서 3가지 경우를 전부 만들어 queue 뒤에 넣고, 그 다음 가장 먼저 들어온 다음 숫자 하나를 꺼내서 또 3가지를 만든다
# -> 이 문제에서 poppleft()를 사용하는 이유
