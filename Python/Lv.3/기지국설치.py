def solution(n, stations, w):
    answer = 0
    position = 1
    coverage = 2 * w + 1
    
    for station in stations:
        start = station - w
        
        if position < start:
            length = start - position
            answer += (length + coverage - 1) // coverage
        position = station + w + 1
        
    if position <= n:
        length = n - position + 1
        answer += (length + coverage - 1) // coverage

    return answer

## 풀이전략, 핵심 아이디어
# 이미 설치된 기지국 사이의 빈 구간의 길이를 계산하여 필요한 기지국 개수 구하기
# 기지국 하나가 커버하는 범위를 구하고, 각 범위의 빈 구간을 채우는 데 필요한 최소 기지국 수 합쳐 리턴 
