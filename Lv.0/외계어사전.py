def solution(spell, dic):
    
    spell = sorted(spell)
    
    for s in dic:
        if sorted(s)==spell:
            return 1
    return 2

## 풀이전략, 핵심 아이디어
# 문자열 정렬한 후 비교하면 됨
# for문으로 계속 돌려야된다고 생각하기만함
# 발상의 전환 필요!!
