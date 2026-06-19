def solution(k, score):
    sc_k = []
    answer = []
    
    for s in score:
        sc_k.append(s)
        sc_k.sort()
        
        if len(sc_k) > k:
            sc_k.pop(0)
            
        answer.append(sc_k[0])
        
    return answer

## 풀이전략, 핵심 아이디어
# 반복문으로 점수를 하나씩 넣고, 정렬시키기
# 그 개수가 k개를 넘는다면 제거
# 정답 리스트에 정렬된 sc_k의 0번째 값을 하나씩 넣기
