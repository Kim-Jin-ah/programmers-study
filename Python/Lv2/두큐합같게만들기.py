from collections import deque
def solution(queue1, queue2):
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    count = 0
    limit = 3 * (len(queue1) + len(queue2))
    while count <= limit:
        if sum1 == sum2:
            return count
        
        if sum1 < sum2:
            x = queue2.popleft()
            queue1.append(x)
            
            sum2 -= x
            sum1 += x
        else:
            x = queue1.popleft()
            queue2.append(x)
            
            sum1 -= x
            sum2 += x
        
        count += 1
        
    return -1

## 풀이전략, 핵심 아이디어
# while 설정할 때, 두 큐의 합이 같아질 때까지 옮기는데, 아예 만들 수 없는 경우 무한 반복하지 않도록 이동 횟수 제한을 둔다.
# sum()을 변수로 두고 활용하며 사용. 계속 sum()으로 사용하면 효율성 떨어짐(계속 sum()을 계산하기 때문에)
