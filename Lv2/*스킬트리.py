def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        skill_list = ""
        for s in skill_tree:
            if s in skill:
                skill_list += s
        
        if skill.startswith(skill_list):
            answer += 1
        
    return answer

## 풀이전략, 핵심 아이디어
# 스킬트리에서 선행 스킬만 뽑았을 때, skill의 앞부분과 똑같은지 검사하는 게 핵심
# 따라서 startswith의 활용이 중요
