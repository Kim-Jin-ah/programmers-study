def solution(begin, target, words):
    if target not in words:
        return 0

    answer = []
    def dfs(word,count,visited):
        if word == target:
            answer.append(count)
            return
        
        for next_word in words:
            diff = 0
            for j in range(len(word)):
                if word[j] != next_word[j]:
                    diff += 1
                    
            if diff == 1 and next_word not in visited:
                visited.add(next_word)
                dfs(next_word,count+1,visited)
                visited.remove(next_word)
                
    dfs(begin,0,set())
    
    return min(answer) if answer else 0
  ## dfs로 풀이한 방법

from collections import deque
def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = deque([(begin,0)])
    visited = {begin}
    
    while queue:
        word,count = queue.popleft()
        
        if word == target:
            return count
        
        for next_word in words:
            if next_word not in visited:
                diff = 0
                for a,b in zip(word,next_word):
                    if a != b:
                        diff += 1
                        
                if diff == 1:
                    visited.add(next_word)
                    queue.append((next_word,count+1))
    return 0
## bfs로 풀이한 방법

## 풀이전략, 핵심 아이디어
# 최소count를 찾는 것이 목적이므로 bfs로 푸는 것이 적합함
# 문제 의도 파악을 우선시 해 어떤 방법이 더 효율적일지 먼저 생각하기
