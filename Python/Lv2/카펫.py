def solution(brown, yellow):
    total = yellow + brown
    
    x = int(total**0.5)
    
    while True:
        if total % x == 0:
            y = total // x
            
            if (x-2)*(y-2) == yellow:
                return [y,x]
        
        x -= 1

## 풀이전략, 핵심 아이디어
# 가로와 세로 중 작은 쪽은 항상 전체칸수의 제곱근 이하이기 때문에, 제곱근부터 내려가면서 약수를 찾는 방식으로 탐색 범위 줄임
# 제곱근이 약수가 아닐 경우를 대비해서 노란색 조건도 검증한 후 결과 반환
