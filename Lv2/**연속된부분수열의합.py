def solution(sequence, k):
    answer = [0,len(sequence)-1]
    left = 0
    total = 0
    
    for right in range(len(sequence)):
        total += sequence[right]
        
        while total > k:
            total -= sequence[left]
            left += 1
            
        if total == k:
            if right - left < answer[1] - answer[0]:
                answer = [left,right]
    
    return answer

## 풀이전략, 핵심 아이디어
# 투포인터 방식
# right를 이동하면서 합에 원소 추가
# 합이 k보다 크면 left 이동, 합이 k와 같다면 조건문을 거친후 [left,right] 저장
