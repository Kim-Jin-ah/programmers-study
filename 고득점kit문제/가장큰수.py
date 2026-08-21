from functools import cmp_to_key
def solution(numbers):
    numbers = list(map(str,numbers))

    def compare(a,b):
        if a + b > b + a:
            return -1
        elif a + b < b + a:
            return 1
        else:
            return 0
    
    numbers.sort(key = cmp_to_key(compare))
    
    if numbers[0] == "0":
        return "0"
    
    return ''.join(numbers)

## 풀이전략, 핵심 아이디어
# cmp_to_key를 활용해 비교함수 설정하여 sort
# compare 함수 설정 후 return 1과 -1 의 역할 암기
