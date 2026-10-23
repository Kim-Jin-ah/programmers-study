def solution(numlist, n):
    answer = []
    answer = sorted(numlist,key = lambda x : (abs(x-n),-x))
    return answer

## 풀이전략, 핵심아이디어
# 람다함수와 sort정렬을 함께 사용하기
# 내림차순(-)과 오름차순 공식 암기
# sort와 sorted 차이 확실히 구분해서 이해하기
