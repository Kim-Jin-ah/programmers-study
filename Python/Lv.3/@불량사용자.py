def solution(user_id, banned_id):
    answer = set()
    
    def dfs(depth,selected):
        if depth == len(banned_id):
            answer.add(tuple(sorted(selected)))
            return
        
        pattern = banned_id[depth]
        for user in user_id:
            if len(user) != len(pattern):
                continue
            match = True
            for i in range(len(user)):
                if pattern[i] != "*" and pattern[i] != user[i]:
                    match = False
                    break
                    
            if match and user not in selected:
                selected.add(user)
                dfs(depth+1,selected)
                selected.remove(user)
                
    dfs(0,set())
    
    return len(answer)

## 풀이전략, 핵심 아이디어
# dfs와 백트래킹, 중복 조합 제거를 이해하는 것이 핵심
# dfs 문제 더 연습하기
