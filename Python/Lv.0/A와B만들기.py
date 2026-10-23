def solution(before, after):
    answer = 0
    if sorted(before) == sorted(after):
        return 1
    else:
        return 0
        
    return answer

## 풀이전략, 핵심아이디어
# 발상의 전환 필요..
# 한가지만 생각말고 다양하게..
# 구성요소 정렬이 아닌 각 요소를 검사해서 같은지 확인하는 방법밖에 생각하지 못한게 실패의 이유....
