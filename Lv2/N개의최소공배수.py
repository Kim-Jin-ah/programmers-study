import math
def solution(arr):
    num = arr[0]

    for i in range(1,len(arr)):
        num = (num*arr[i]) // math.gcd(num,arr[i])
        
    return num

## 풀이전략, 핵심 아이디어
# N개의 숫자를 한꺼번에 처리가 아닌, 첫번째 결과 + 다음 숫자 를 계속 합치는 게 포인트
