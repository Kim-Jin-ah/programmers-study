def solution(absolutes, signs):
    answer = 0
    
    for i in range(len(absolutes)):
        if signs[i]:
            answer += absolutes[i]
        else:
            answer -= absolutes[i]
    
    return answer

## 풀이전략, 핵심 아이디어
# 범위를 absolutes의 len 으로 잡기
# if문의 true, false 결과값에 맞는 조건 적고 더하기 혹은 빼기로 계산
