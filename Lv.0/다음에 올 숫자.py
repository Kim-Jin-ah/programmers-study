def solution(common):
    answer = 0
    if common[1]-common[0] == common[2]-common[1]:
        answer=common[-1]+(common[1]-common[0])
    else:
        answer=common[-1]*(common[1]-common[0])
    
    return answer

# 마지막 순서의 숫자를 찾을 때 -1 인 것 유의하기!
# 각 원소를 반복문으로 빼서 각각 생각하는 것이 아닌 common 자체에서 해결할 수 있는지 먼저 확인했어야함
#
