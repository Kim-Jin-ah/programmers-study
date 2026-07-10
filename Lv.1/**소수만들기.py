def solution(nums):
    answer = 0
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
            for k in range(j+1,len(nums)):
                total = nums[i] + nums[j] + nums[k]
                
                prime = True
                for x in range(2, int(total**0.5)+1):
                    if total % x == 0:
                        prime = False
                        break
                if prime:
                    answer += 1
                    
    return answer

## 반복문 3개를 combinations로 쓸 수 있음
from itertools import combinations

for comb in combinations(nums,3):
  total = sum(comb)

## 풀이전략, 핵심 아이디어
# 반복문 3개를 이용하여 중복없이 3개를 뽑고, total에 3개의 합 저장
# true, false를 이용해 소수 거르기
