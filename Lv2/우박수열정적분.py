def solution(k, ranges):
    arr = [k]
    while k > 1:
        if k % 2 == 0:
            k //= 2   
        else:
            k = k * 3 + 1
        arr.append(k)
    
    n = len(arr)-1
    answer = []
    for a,b in ranges:
        start = a
        end = n + b
        
        if start > end:
            answer.append(-1.0)
            continue
        
        total = 0
        for i in range(start,end):
            total += (arr[i] + arr[i+1]) / 2
        answer.append(total)
    return answer

## 풀이전략, 핵심 아이디어
# 누적합을 활용하여 구간합 구하기, 예외처리 신경쓰기
