def solution(n):
    answer = 0
    for i in range(2,n+1):
        count = 0
        for j in range(1,i+1):
            if i % j == 0:
                count += 1
        if count == 2:
            answer += 1
    return answer

## 효율성 부분에서 많이 떨어짐..
## 하나씩 찾는게 아닌 소수가 아닌 수들을 제거하면서 찾는 방식으로 바꾸는게 효율적. 따라서
## '에라토스테네스의 채'사용 (소수를 하나씩 찾는것이 아닌, 소수가 아닌수를 한번에 지워나가는 방식) 
def solution(n):
    prime = [True] * (n+1)
    
    for i in range(2, int(n**0.5)+1):
        if prime[i]:
            for j in range(i*i,n+1,i):
                prime[j] = False
    
    return sum(prime[2:])
