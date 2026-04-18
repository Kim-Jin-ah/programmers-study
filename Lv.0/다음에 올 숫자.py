def solution(common):
    answer = 0
    if common[1]-common[0] == common[2]-common[1]:
        answer=common[-1]+(common[1]-common[0])
    else:
        answer=common[-1]*(common[1]//common[0])
    
    return answer

## 풀이전략, 핵심아이디어
# 마지막 순서의 숫자를 찾을 때 -1 인 것 유의하기!
# 각 원소를 반복문으로 빼서 각각 생각하는 것이 아닌 common 자체에서 해결할 수 있는지 먼저 확인했어야함
# 공비라면 곱하는 것과 더불어 차이를 계산할 때 나누기를 해야한다는 점 유의하기!

# 만약 등차수열이라면, 마지막 순서의 값에 등차만큼 더해주기
# 만약 등비수열이라면, 마지막 순서의 값에 등비만큼 곱해주기
