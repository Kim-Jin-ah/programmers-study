def solution(picks, minerals):
    total_picks = sum(picks)
    max_minerals = total_picks * 5
    if len(minerals) > max_minerals:
        minerals = minerals[:max_minerals]
    
    groups = []
    for i in range(0,len(minerals),5):
        arr = minerals[i:i+5]
        dia = arr.count("diamond")
        iron = arr.count("iron")
        stone = arr.count("stone")
        groups.append((dia,iron,stone))

    groups.sort(key = lambda x : (x[0]*25 + x[1]*5 + x[2]),reverse=True)
    
    answer = 0
    dia_pick, iron_pick, stone_pick = picks

    for dia, iron, stone in groups:
        if dia_pick > 0:
            answer += (dia + iron + stone)
            dia_pick -= 1
        elif iron_pick > 0:
            answer += (dia * 5 + iron + stone)
            iron_pick -= 1
        elif stone_pick > 0:
            answer += (dia * 25 + iron * 5 + stone)
            stone_pick -= 1
        else:
            break
            
    return answer

## 풀이전략, 핵심 아이디어
# 5개씩 묶고 우선순위 정렬 이 핵심
# 어느 곡괭이를 어느 구간에 써야 전체 피로도를 최소화할 수 있을지 판단하는 것이 중요한 문제
