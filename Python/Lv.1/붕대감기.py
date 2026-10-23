def solution(bandage, health, attacks):
    now = health
    success = 0
    attack_idx = 0
    last = attacks[-1][0]
    
    for time in range(1,last+1):
        if attack_idx < len(attacks) and time == attacks[attack_idx][0]:
            now -= attacks[attack_idx][1]
            success = 0
            
            if now <= 0:
                return -1
            
            attack_idx += 1
            
        else:
            now = min(now + bandage[1],health)
            success += 1
            
            if success == bandage[0]:
                now = min(now + bandage[2],health)
                success = 0
    return now

## 풀이전략, 핵심 아이디어
# 현재 체력 now를 최대체력 health로 초기화 후 시간을 1초부터 마지막 공격 시간까지 1초씩 증가시킴
# 현재 시간이 공격 시간일 때와 아닐 때를 조건문으로 판단, 결과 return
## 1초씩 시간을 흘려보내며 시뮬레이션!
