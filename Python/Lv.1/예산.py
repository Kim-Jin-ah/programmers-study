def solution(d, budget):
    d_sum = 0
    count = 0
    for i in sorted(d):
        count += 1
        d_sum += i
        if d_sum > budget:
            count -= 1
            break
            
    return count

## 풀이 전략, 핵심 아이디어
# 작은 금액부터 순회한뒤
# 현재까지 지원한 금액 계산 후 지원 부서 수 count에 +1씩 증가시키기
# 예산 초과가 확인된다면 바로 전 부서 취소(count-1)
