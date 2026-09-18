from math import gcd
from functools import reduce
def solution(arrayA, arrayB):
    gcdA = reduce(gcd,arrayA)
    gcdB = reduce(gcd,arrayB)
    
    answer = 0
    
    if all(num % gcdA != 0 for num in arrayB):
        answer = max(answer,gcdA)
        
    if all(num % gcdB != 0 for num in arrayA):
        answer = max(answer,gcdB)
        
    return answer

## 풀이전략, 핵심 아이디어
# A배열,B배열 각각 전체의 최대공약수 구하기
# 그 숫자가 다른 배열의 모든 숫자를 나누지 못하는지 확인
# 조건을 만족하면 정답 후보에 저장
# 최대공약수 math.gcd()와 reduce() 함수 익히기
