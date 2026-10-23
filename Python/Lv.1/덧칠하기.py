def solution(n, m, section):
    answer = 0
    paint = 0
    
    for i in section:
        if i > paint:
            answer += 1
            paint = i + m - 1
        
    return answer

## 풀이전략, 핵심 아이디어
# 그리디 문제로 '안칠해진 구역을 만나면 그 자리에서 바로 최대한 길게 칠하는 것이 최선' 임을 생각하는 게 핵심
# 현재 어디까지 칠했는지를 저장하는 상태를 나타내는 paint 변수를 만들어 접근!!
