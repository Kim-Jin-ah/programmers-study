def solution(sides):
    answer = 0
    sorted_sides = sorted(sides)

    if sorted_sides[2] < sorted_sides[0]+sorted_sides[1]:
        return 1
    else:
        return 2
    
    return answer

## 풀이전략, 핵심아이디어
# 최대치와 나머지의 구분을 리스트 정렬로!!
# 아이디어 떠올리는 노력... 더 하자..
