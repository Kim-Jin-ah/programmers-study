def solution(nums):
    answer = 0
    count = []
    
    for i in nums: 
        if i not in count:
            count.append(i)
        
    if len(count) >= len(nums)//2:
        answer += (len(nums)//2)
    else:
        answer += len(count)
    
    return answer
  
## 풀이전략, 핵심 아이디어
# 풀이를 단순하게 할 수 있는 방법 찾기
# 중복을 제거하고 최소를 찾는 것이 핵심이기 때문에
# 최소 찾는 방법을 좀 더 쉽게 바꾼다면
def solution(nums):
    count = []
    
    for i in nums: 
        if i not in count:
            count.append(i)
        
    return min(len(count),len(nums)//2)
  
# 여기서 중복제거를 set()으로 활용한다면
def solution(nums): 
    return min(len(set(nums)),len(nums)//2)
# 좀더 간단하고 쉽게 풀 수 있는 방법 같이 고민해보기
