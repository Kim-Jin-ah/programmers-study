def solution(n):
    answer = 0
    
    for i in range(1, n+1):
        count = 0
        
        for j in range(1,i+1):
            if i%j == 0:
                count += 1
            
        if count >= 3:
            answer += 1
            
    return answer

## 풀이전략, 핵심 아이디어
# 반복문으로 약수 개수 구하기
# 반복문 안에 반복문을 사용해서 n 이하 합성수 개수를 구해야한다는 것이 특징
