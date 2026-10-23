def solution(left, right):
    answer = 0
    
    for i in range(left, right+1):
        count = 0
        for num in range(1,i+1):
            if i % num == 0:
                count += 1
                
        if count % 2 == 0:
            answer += i
        else:
            answer -= i
            
    return answer

## 풀이 전략, 핵심 아이디어
# count = 0 을 반복문 안에 넣어야 한다는 것이 핵심!!
# 반복문 밖과 안의 두는 차이를 잘 알아두어야 함
