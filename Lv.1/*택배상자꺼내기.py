def solution(n, w, num):
    answer = 0
    arr = [[] for _ in range(w)]
    
    for i in range(1,n+1):
        row = (i-1) // w
        col = (i-1) % w
        
        if row % 2 == 0:
            arr[col].append(i)
        else:
            arr[w-1-col].append(i)
            
    for col in range(w):
        if num in arr[col]:
            target_col = col
            break
    
    idx = arr[target_col].index(num)
    
    answer = len(arr[target_col]) - idx
    
    return answer

## 풀이전략, 핵심 아이디어
# 리스트를 만들어서 상자의 위치를 저장. 세로줄 기준 이중 리스트 만들기가 핵심.
# 이 풀이는 5번은 돌려보고 외우기. 문제풀이구상에 도움될 것.
