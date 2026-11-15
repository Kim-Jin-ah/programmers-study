def solution(routes):
    routes.sort(key = lambda x : x[1])
    camera = -30001
    answer = 0
    
    for start,end in routes:
        if camera < start:
            answer += 1
            camera = end
            
    return answer

## 풀이전략, 핵심 아이디어
# 진출 지점 기준으로 오름차순 정렬로 다른 차량의 경로와 겹칠 확률 최대화
# 반복문에서 카메라 위치 갱신 및 카운트
